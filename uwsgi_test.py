def application(enviroment, start_response):
    """接收两个参数, 一个是环境, 一个是"""
    start_response('200 OK', [('Content-Type','text/html')])
    print(enviroment)
    print(start_response)
    return [b"Hello World"]