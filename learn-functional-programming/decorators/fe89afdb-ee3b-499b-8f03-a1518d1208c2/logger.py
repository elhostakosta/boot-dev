def args_logger(*args, **kwargs):
    line_number = 1
    
    for arg in args:
        print(f"{line_number}. {arg}")
        line_number += 1
        
    kwargs = dict(sorted(kwargs.items()))
    
    for kwarg in kwargs:
        print(f"* {kwarg}: {kwargs[kwarg]}")
