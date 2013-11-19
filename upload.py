import tornado.ioloop
import tornado.web


class UploadHandler(tornado.web.RequestHandler):
    """ Upload files """
    def get(self):
        self.render("upload.html")

    def post(self):
        filenames = []

        if hasattr(self.request,'files'):
            for file in self.request.files.get('files',[]):
                filename = file['filename']
                output_file = open("files/" + filename, 'w')
                output_file.write(str(file['body']))
                filenames.append(filename)

        if len(filenames) > 1:
            self.finish("Files " + "; ".join(filenames) + " are uploaded")
        elif len(filenames) == 1:
            self.finish("File " + filenames[0] + " is uploaded")
        else:
            self.finish("Any files are uploaded")


application = tornado.web.Application([
    (r"/upload", UploadHandler),
    ])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
