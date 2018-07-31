if __name__ == '__main__':
    module = __import__('celue')
    import inspect
    print inspect.getmembers(module, inspect.isclass)
    print getattr(module,'BulkItemPromo')