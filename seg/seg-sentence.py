import web
import sys

# 引入jieba类库包
import jieba
import jieba.posseg
import jieba.analyse

# http访问影射（对应的处理类）
urls = (
    '/index', 'index',
    '/test', 'test',
)

# 初始化web app
app = web.application(urls, globals())

# 解决返回乱码问题
web.header('Content-Type','text/json; charset=utf-8', unique=True)

# 定义处理/index的请求
class index:
    def GET(self):
        params = web.input()
        # 获取请求参数context
        input_context = params.get('context', '')
        # 使用jieba对输入参数分词
        seg_context = jieba.cut(input_context)
        # jieba分词返回的是一个list，通过join的方式连接为字符串
        return_context = ",".join(seg_context)
        return return_context

#定义出路/test的请求
class test:
    def GET(self):
        print web.input()
        return 'the first webpy application from test'

if __name__ == '__main__':
    app.run()