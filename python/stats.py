def get_book_wc(filepath):
        with open(filepath) as f:
                text = f.read()
                words = text.split(" ")
                wc = 0
                for word in words:
                        wc += 1
        return wc
