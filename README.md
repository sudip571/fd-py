#Installation


To list the sub-modules inside your installed package
import pkgutil
import flightdeckpy

# iter_modules looks at the path of your installed package
modules = [name for _, name, _ in pkgutil.iter_modules(flightdeckpy.__path__)]
print(modules)