class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<a>")

        for data in self.datas:
            # 屏蔽掉原来的，重新写一个更美观的输出效果
            # fout.write("<tr>")
            # fout.write("<td>%s</td>" % data['url'])
            # fout.write("<td>%s</td>" % data['title'])
            # fout.write("<td>%s</td>" % data['summary'])
            # fout.write("</tr>")
            fout.write('<a href="%s">%s</a>' % (data['url'], data['title']))
            fout.write('<p>%s</p>' % data['summary'])

        fout.write("</a>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()
