import visa
import numpy as np
from math import log
import csv
import sys

from enum import Enum
class State(Enum):
    OFF = 0
    ON = 1

class e4980al:
    def __init__(self, auto_choose = False):
        self.e4980al_usb_id = "0x0957::0x0909"
        instrument_visa_identifier = self.select_instrument(auto_choose)
        if instrument_visa_identifier is None:
            raise Exception
        self.init_instrument(instrument_visa_identifier)

        self.bias = 0.0

    def select_instrument(self, auto_choose):
        found_count = 0
        rm = visa.ResourceManager()
        reslist = rm.list_resources()
        e4980al_dict = {}
        for r in reslist:
            if self.e4980al_usb_id in r:
                e4980al_dict[found_count] = r
                found_count += 1
        if found_count == 0:
            visa_address =  None
        elif auto_choose or found_count == 1:
            visa_address = e4980al_dict[0]
            print("Auto selected instument: {}".format(visa_address))
        else:
            for idx, r in e4980al_dict.items():
                print("({idx}), {res_name}".format(idx=idx+1, res_name=r))
            i = int(input("Which instument?: ")) - 1
            visa_address = e4980al_dict[i]
            print("Selected instument: {}".format(visa_address))

        return visa_address



    def init_instrument(self, instrument_visa_identifier):
        rm = visa.ResourceManager()
        my_instrument = rm.open_resource(instrument_visa_identifier)
        self.inst = my_instrument

    def meas_type(self, meas_type):
        #
        # Syntax:
        # :FUNCtion:IMPedance[:TYPE]
        # {CPD|CPQ|CPG|CPRP|CSD|CSQ|CSRS|LPD|LPQ|LPG|LPRP|LPRD|LSD|LSQ|LSRS|LSRD|RX|ZTD|ZTR|GB|YTD|YTR|VDID}

        if self.meas_type_valid(meas_type):
            print("Measurement type: " + meas_type.upper())
            self.write(":FUNC:IMP {}".format(meas_type.upper()))
        else:
            print("INVALID! measurement type: " + meas_type.upper(), file=sys.stderr)

    def meas_type_valid(self, meas_type):
        available_meas_types = ["CPD", "CPQ", "CPG", "CPRP", "CSD", "CSQ", "CSRS", "LPD", "LPQ", "LPG", "LPRP", "LPRD", "LSD", "LSQ", "LSRS",
         "LSRD", "RX", "ZTD", "ZTR", "GB", "YTD", "YTR", "VDID"]
        if meas_type.upper() in available_meas_types:
            return True
        else:
            return False

    def set_meas_freq(self, hz):
        if 20 <= hz and hz <= 1e6:
            self.inst.write(":FREQ:CW {}".format(hz))
        else:
            print("INVALID! Out of range", file=sys.stderr)

    def set_meas_voltage(self, voltage):
        if self.bias + 0.0 <= voltage and voltage <= self.bias + 2.0:
            self.inst.write(":VOLT:LEV {}".format(voltage))
        else:
            print("INVALID! Out of range", file=sys.stderr)

    def set_bias_voltage(self, voltage):
        self.bias = voltage
        self.inst.write(":BIAS:VOLT:LEV {}".format(voltage))

    def set_trig_mode(self, trig_mode):
        # Syntax
        # :TRIGger:SOURce {INTernal|HOLD|EXTernal|BUS}
        # :TRIGger:SOURce?
        self.inst.write(":TRIG:SOUR {}".format(trig_mode))

    def trigger(self):
        # Syntax
        # TRIGger[:IMMediate]
        self.inst.write(":TRIG:IMM")

    def aperture(self, time, average):
        # Syntax
        # :APERture {SHORt | MEDium | LONG}, < numeric >
        # :APERture?
        self.inst.write(":APER {},{}".format(time,average))

    def clear_display(self):
        self.inst.write(":DISP:CCL")

    def enable_display(self, state):
        # Syntax:
        # DISPlay:ENABle {ON | OFF | 1 | 0}
        # :DISPlay: ENABle?
        self.inst.write(":DISP:ENAB {}".format(state))

    def set_comment(self, comment):
        # Syntax:
        # :DISPlay:LINE <String>
        # :DISPlay:LINE?
        if len(comment) <= 30:
            self.inst.write(":DISP:LINE \"{}\"".format(comment))
        else:
            print("INVALID! Max. 30 ASCII chars allowed", file=sys.stderr)

    def disp_page(self, page):
        '''
        Syntax: DISPlay:PAGE
        :MEASurement | BNUMber | BCOunt | LIST | MSETup | CSETup | LTABle | LSETup | CATAlog | SYSTem | SELF | MLARge | SCONfig | SERVice}
        :DISPlay: PAGE?

        MEASurement (Preset value) Sets displayed page to <MEAS DISPLAY>
        BNUMber Sets displayed page to <BIN No. DISPLAY>
        BCOunt Sets displayed page to <BIN COUNT DISPLAY>
        LIST Sets displayed page to <LIST SWEEP DISPLAY>
        MSETup Sets displayed page to <MEAS SETUP>
        CSETup Sets displayed page to <CORRECTION>
        LTABle Sets displayed page to <LIMIT TABLE SETUP>
        LSETup Sets displayed page to <LIST SWEEP SETUP>
        CATAlog Sets displayed page to <CATALOG>
        SYSTem Sets displayed page to <SYSTEM INFO>
        SELF Sets display page to <SELF TEST>
        MLARge Sets page to display measurement results in large
        characters
        SCONfig Sets displayed page to <SYSTEM CONFIG>
        SERVice Sets displayed page to <SERVICE>

        :param page:
        :return:
        '''
        self.inst.write(":DISP:PAGE {}".format(page))


    def get_log_list(self, from_val, to_val, number_of_steps):
        base = 10.0
        logsp = np.logspace(log(from_val, base), log(to_val, base), num=number_of_steps, endpoint=True, base=base,
                            dtype=None)
        return logsp

    def get_lin_list(self, from_val, to_val, number_of_steps):
        linsp = np.linpace(from_val, to_val, num=number_of_steps, endpoint=True, dtype=None)
        return linsp


    def fetch(self):
        str = self.inst.query(":FETC?")
        l = str.split(",")
        l = list(map(float, l))
        return l

    def beep_type(self, beep_t):
        self.inst.query(":SYSTem:BEEPer:TONE {}".format(beep_t))

    def beep_enable(self, state):
        # Syntax:
        # :SYSTem:BEEPer: STATe {ON | OFF | 1 | 0}
        # :SYSTem: BEEPer:STATe?
        self.inst.query(":SYSTem:BEEPer:STATe {}".format(state))

    def beep(self):
        self.inst.write(":SYSTem:BEEPer:IMMediate")

    def meas_point(self, hz, voltage):
        self.set_meas_freq(hz)
        str = self.inst.query(":FETC?")
        l = str.split(",")
        l = list(map(float, l))
        m1 = l[0]
        m2 = l[1]
        return hz, m1, m2



    def manual_list_measure(self, meas_type, from_hz, to_hz, steps):
        l = []
        self.meas_type(meas_type)
        for i in self.get_log_list(from_hz,to_hz,steps):
            m = self.meas_point(i)
            l.append(m)

        return  l

def save_as_csv(list_of_results, filename, header=None):
    with open(filename, "w") as f:
        csv_out = csv.writer(f)
        if header is not None:
            csv_out.writerow(header)
        for row in list_of_results:
            csv_out.writerow(row)


if __name__ == "__main__":
    muszer = e4980al()
    x = muszer.manual_list_measure("CSRS", 20, 1e6, 200)
    save_as_csv(x, "teszt.csv")


