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

def run_basic_struct_empty():
    val = "type unTipo struct {}"
    res = run_test(val)
    print(res)

### TWO STRUCT
def run_two_structs():
    val = "type unTipo struct {unNumero int unaPalabra string unFlotante float64 unBooleano bool laDependencia otroTipo} type otroTipo struct {unNumero int unaPalabra string unFlotante float64 unBooleano bool} "
    res = run_test(val)
    print(res)

def run_two_structs_with_inline_struct():
    val = "type unTipo struct {unNumero int unaPalabra string unFlotante float64 unBooleano bool unStruct struct {unNumerito int laDependencia otroTipo}} type otroTipo struct {unNumero int unaPalabra string unFlotante float64 unBooleano bool}"
    res = run_test(val)
    print(res)

def run_two_structs_with_array():
    val = "type unTipo struct {unNumero int unaPalabra []string unFlotante []float64 unBooleano bool unStruct struct {unNumerito []int laDependencia []otroTipo}} type otroTipo struct {unNumero int unaPalabra string unFlotante []float64 unBooleano bool}"
    res = run_test(val)
    print(res)

def run_two_structs_with_array_of_array():
    val = "type unTipo struct {unNumero int unaPalabra []string unFlotante []float64 unBooleano bool unStruct struct {unNumerito []int laDependencia [][]otroTipo}} type otroTipo struct {unNumero int unaPalabra string unFlotante []float64 unBooleano bool}"
    res = run_test(val)
    print(res)

def run_two_structs_with_array_of_inline_struct():
    val = "type unTipo struct {unNumero int unaPalabra []string unFlotante [][]float64 unBooleano bool unStruct struct {unNumerito []int laDependencia otroTipo}} type otroTipo struct {unNumero int unaPalabra string unFlotante []float64 unBooleano bool}"
    res = run_test(val)
    print(res)

def run_two_structs_with_array_of_inline_struct():
    val = "type unTipo struct {unNumero int unaPalabra []string unFlotante []float64 unBooleano bool unStruct []struct {unNumerito []int laDependencia []otroTipo}} type otroTipo struct {unNumero int unaPalabra string unFlotante []float64 unBooleano bool}"
    res = run_test(val)
    print(res)

def run_two_structs_empty():
    val = "type unTipo struct {laDependencia otroTipo} type otroTipo struct {}"
    res = run_test(val)
    print(res)

## THREE STRUCT
def run_three_structs():
    val = "type unTipo struct {unNumero int unaPalabra string unFlotante float64 unBooleano bool laDependencia otroTipo} type otroTipo struct {otraDependencia ultimoTipo unaPalabra string unFlotante float64 unBooleano bool} type ultimoTipo struct {ultimoInt int ultimoString []string} "
    res = run_test(val)
    print(res)

def run_three_structs_with_inline_struct():
    val = "type unTipo struct {unNumero int unaPalabra string unFlotante float64 unBooleano bool unStruct struct {unNumerito int laDependencia otroTipo}} type otroTipo struct {otraDependencia ultimoTipo unaPalabra string unFlotante float64 unBooleano bool} type ultimoTipo struct {ultimoInt int ultimoString []string} "
    res = run_test(val)
    print(res)

def run_three_structs_with_array():
    val = "type unTipo struct {unNumero int unaPalabra string unFlotante float64 unBooleano bool unStruct struct {unNumerito int laDependencia []otroTipo}} type otroTipo struct {otraDependencia []ultimoTipo unaPalabra string unFlotante float64 unBooleano bool} type ultimoTipo struct {ultimoInt int ultimoString []string} "
    res = run_test(val)
    print(res)

def run_three_structs_with_array_of_array():
    val = "type unTipo struct {unNumero int unaPalabra string unFlotante float64 unBooleano bool unStruct struct {unNumerito int laDependencia [][]otroTipo}} type otroTipo struct {otraDependencia [][]ultimoTipo unaPalabra string unFlotante float64 unBooleano bool} type ultimoTipo struct {ultimoInt int ultimoString []string} "
    res = run_test(val)
    print(res)

def run_three_structs_with_array_of_inline_struct():
    val = "type unTipo struct {unNumero int unaPalabra string unFlotante float64 unBooleano bool unStruct []struct {unNumerito int laDependencia []otroTipo}} type otroTipo struct {otraDependencia []ultimoTipo unaPalabra string unFlotante float64 unBooleano bool} type ultimoTipo struct {ultimoInt int ultimoString []string} "
    res = run_test(val)
    print(res)

def run_three_structs_empty():
    val = "type unTipo struct {unNumero int unaPalabra string unFlotante float64 unBooleano bool laDependencia otroTipo} type otroTipo struct {otraDependencia []ultimoTipo unaPalabra string unFlotante float64 unBooleano bool} type ultimoTipo struct {} "
    res = run_test(val)
    print(res)

def run_invalid_typename_mayus():
    try:
        val = "type Untipo struct {}"
        res = run_test(val)
    except Exception as e:
        print("\n***EXCEPTION WAS THROWN***\n")

def run_invalid_typename_number():
    try:
        val = "type 0ntipo struct {}"
        res = run_test(val)
    except Exception as e:
        print("\n***EXCEPTION WAS THROWN***\n")

def run_invalid_typename_reserved_word():
    try:
        val = "type string struct {}"
        res = run_test(val)
    except Exception as e:
        print("\n***EXCEPTION WAS THROWN***\n")

def run_invalid_attribute_mayus():
    try:
        val = "type tipoDefinido struct {Mivalor int}"
        res = run_test(val)
    except Exception as e:
        print("\n***EXCEPTION WAS THROWN***\n")

def run_invalid_attribute_number():
    try:
        val = "type tipoDefinido struct {0ivalor int}"
        res = run_test(val)
    except Exception as e:
        print("\n***EXCEPTION WAS THROWN***\n")

def run_invalid_attribute_reserved_word():
    try:
        val = "type tipoDefinido struct {string int}"
        res = run_test(val)
    except Exception as e:
        print("\n***EXCEPTION WAS THROWN***\n")

def run_invalid_redefine_defined():
    try:
        val = "type tipoDefinido struct {valor int} type tipoDefinido struct {valor int}"
        res = run_test(val)
    except Exception as e:
        print("\n***EXCEPTION WAS THROWN***\n")

def run_invalid_circular_definition_two_struct():
    try:
        val = "type tipoDefinido struct {valor otroTipo} type otroTipo struct {valorcito tipoDefinido}"
        res = run_test(val)
    except Exception as e:
        print("\n***EXCEPTION WAS THROWN***\n")

def run_invalid_circular_definition_three_struct():
    try:
        val = "type tipoDefinido struct {valor otroTipo} type otroTipo struct {valorcito ultimoTipo} type ultimoTipo struct {esteValor tipoDefinido}"
        res = run_test(val)
    except Exception as e:
        print("\n***EXCEPTION WAS THROWN***\n")

def run_invalid_circular_definition_struct_inline():
    try:
        val = "type tipoDefinido struct {valor otroTipo} type otroTipo struct {valorcito ultimoTipo} type ultimoTipo struct {esteValor struct {tipito tipoDefinido}}"
        res = run_test(val)
    except Exception as e:
        print("\n***EXCEPTION WAS THROWN***\n")

'''run_basic_struct()
run_basic_struct_with_inline_struct()
run_basic_struct_with_array()
run_basic_struct_with_array_of_array()
run_basic_struct_with_array_of_inline_struct()
run_basic_struct_empty()

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
run_invalid_attribute_reserved_word()

run_invalid_redefine_defined()
run_invalid_circular_definition_two_struct()
run_invalid_circular_definition_three_struct()
run_invalid_circular_definition_struct_inline()
'''
