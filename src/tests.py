import subprocess
def run_test(val):
    quoted_val = "\"" + val + "\""
    return subprocess.check_output('python3 parser.py %s' % quoted_val, shell=True).decode('UTF-8')

### TESTS

### BASIC STRUCT
def run_basic_struct():
    val = "type unTipo struct {unNumero int unaPalabra string unFlotante float64 unBooleano bool}"
    res = run_test(val)
    print(res)

def run_basic_struct_with_inline_struct():
    val = "type unTipo struct {unNumero int unaPalabra string unFlotante float64 unBooleano bool unStruct struct {unNumerito int unBooleanito bool}}"
    res = run_test(val)
    print(res)

def run_basic_struct_with_array():
    val = "type unTipo struct {unNumero int unaPalabra []string unFlotante []float64 unBooleano bool unStruct struct {unNumerito []int unBooleanito bool}}"
    res = run_test(val)
    print(res)

def run_basic_struct_with_array():
    val = "type unTipo struct {unNumero int unaPalabra []string unFlotante []float64 unBooleano bool unStruct struct {unNumerito []int unBooleanito bool}}"
    res = run_test(val)
    print(res)

def run_basic_struct_with_array_of_array():
    val = "type unTipo struct {unNumero int unaPalabra []string unFlotante [][]float64 unBooleano bool unStruct struct {unNumerito []int unBooleanito bool}}"
    res = run_test(val)
    print(res)

def run_basic_struct_with_array_of_inline_struct():
    val = "type unTipo struct {unNumero int unaPalabra []string unFlotante []float64 unBooleano bool unStruct []struct {unNumerito []int unBooleanito bool}}"
    res = run_test(val)
    print(res)


run_basic_struct()
run_basic_struct_with_inline_struct()
run_basic_struct_with_array()
#run_basic_struct_with_array_of_array()
run_basic_struct_with_array_of_inline_struct()
'''run_basic_struct_empty()

run_two_structs()
run_two_structs_with_inline_struct()
run_two_structs_with_array()
run_two_structs_with_array_of_array()
run_two_structs_with_array_of_inline_struct()
run_two_structs_empty()

run_three_structs()
run_three_structs_with_inline_struct()
run_three_structs_with_array()
run_three_structs_with_array_of_array()
run_three_structs_with_array_of_inline_struct()
run_three_structs_empty()

run_invalid_typename_mayus()
run_invalid_typename_number()
run_invalid_typename_reserved_word()
run_invalid_attribute_mayus()
run_invalid_attribute_number()
run_invalid_attribute_reserved_word()'''
