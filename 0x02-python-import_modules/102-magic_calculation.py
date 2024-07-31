def magic_calculation(a, b):
    # Importing functions from the module `magic_calculation_102`
    from magic_calculation_102 import add, sub

    # Check if `a` is less than `b`
    if a < b:
        # Initial calculation using the `add` function
        c = add(a, b)
        # Loop over the range from 4 to 6 (inclusive)
        for i in range(4, 6):
            # Update `c` using the `add` function
            c = add(c, i)

        # Return the final value of `c`
        return c
    else:
        # If `a` is not less than `b`, use the `sub`
        # function and return its result
        return sub(a, b)
