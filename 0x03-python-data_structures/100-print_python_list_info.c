#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, allocated, i;
    PyObject *item;

    if (!PyList_Check(p))
        return;

    size = PyList_Size(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

int main(int ac, char **av)
{
    Py_Initialize();
    PyObject *my_list;
    my_list = Py_BuildValue("[s, i, i, i, i]", "Hello", 4, 3, 2, 1);

    print_python_list_info(my_list);

    Py_Finalize();
    return (0);
}
