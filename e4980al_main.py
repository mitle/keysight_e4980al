
import sys
from keysight_e4980al import e4980al
import e4980al_gui_support
from si_prefix import si_format

muszer = e4980al(auto_choose=True)

def units_in_mode(mode):
    ohm = 'Ω'
    farad = 'F'
    siemens = 'S'
    henry = 'H'
    mode_unit_dict = {   "CPD":(farad, ""),
                         "CPQ":(farad, ""),
                         "CPG":(farad, siemens),
                         "CPRP":(farad, ohm),
                         "CSD":(farad, ""),
                         "CSQ":(farad, siemens),
                         "CSRS":(farad, ohm),
                         "LPD":(henry, ""),
                         "LPQ":(henry, ""),
                         "LPG":(henry, siemens),
                         "LPRP":(henry, ohm),
                         "LPRD":(henry, ohm),
                         "LSD":(henry, ""),
                         "LSQ":(henry, ""),
                         "LSRS":(henry, ohm),
                         "LSRD":(henry, ohm),
                         "RX":(ohm, ohm),
                         "ZTD":("", ""),
                         "ZTR":("", ""),
                         "GB":("", ""),
                         "YTD":("", ""),
                         "YTR":("", ""),
                         "VDID":("", "")}
    return mode_unit_dict[mode]

def start_single_measure():
    print('e4980al_gui_support.start_single_measure')
    muszer.set_trig_mode("HOLD")
    meas_mode = meas1.get()
    muszer.meas_type( meas_mode)
    muszer.set_meas_voltage(float(voltage.get()))
    muszer.set_meas_freq(float(freq.get()))
    muszer.disp_page("MEASurement")
    muszer.trigger()
    l = muszer.fetch()
    print('{value1}{unit1}, {value2}{unit2}'.format(value1=si_format(l[0]), unit1=units_in_mode(meas_mode)[0], value12=si_format(l[1]), unit2=units_in_mode(meas_mode)[1]))
    sys.stdout.flush()