try:
    import numpy
    print("✅ NumPy is installed. Version:", numpy.__version__)
except ImportError:
    print("❌ NumPy is NOT installed.")
