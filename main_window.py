import tkinter as tk
from url_client import UrlClient
from wiki_parser import WikiParser


class MainWindow(tk.Frame):
    def __init__(self, parent: tk.Tk) -> None:
        super().__init__(parent)
        self.parent = parent
        self.url = 'https://en.wikipedia.org/wiki/Main_Page'
        self.url_client = UrlClient()
        self.wiki_parser = WikiParser()
        self.init_window()
        self.init_widgets()
        self.organize_widgets()

    def init_window(self) -> None:
        self.parent.title('Scrap Wiki')
        self.parent.geometry("800x600")

    def init_widgets(self) -> None:
        self.connectButton = tk.Button(self.parent, text="Connect to wikipedia", command=lambda: self.get_info(self.url))
        self.label_otd = tk.Label(self.parent, text="On this day:")
        self.label_feat_article = tk.Label(self.parent, text="Feature article:")
        self.text_otd = tk.Text(self.parent, wrap='word')
        self.text_feat_article = tk.Text(self.parent, wrap='word')
        self.scroll_bar_otd = tk.Scrollbar(self.parent, orient='vertical')
        self.scroll_bar_feat = tk.Scrollbar(self.parent, orient='vertical')
        # scrollbars
        self.text_otd.config(yscrollcommand=self.scroll_bar_otd.set)
        self.scroll_bar_otd.config(command=self.text_otd.yview)
        self.text_feat_article.config(yscrollcommand=self.scroll_bar_feat.set)
        self.scroll_bar_feat.config(command=self.text_feat_article.yview)

    def organize_widgets(self) -> None:
        # Packing area
        self.connectButton.grid(row=1, column=1)
        self.label_otd.grid(row=2, column=1)
        self.text_otd.grid(row=3, column=1, padx=20, stick='nse')
        self.label_feat_article.grid(row=2, column=2)
        self.text_feat_article.grid(row=3, column=2, padx=20, stick='nse')
        self.scroll_bar_otd.grid(row=3, column=1, stick='nse')
        self.scroll_bar_feat.grid(row=3, column=2, stick='nse')
        # configure rows
        self.parent.grid_rowconfigure(1, minsize=20)
        self.parent.grid_rowconfigure(2, minsize=20)
        self.parent.grid_rowconfigure(3, weight=1)

    def set_text_widget_content(self, widget: tk.Text, content: str) -> None:
        widget.delete(1.0, 'end')
        widget.insert('end', content)

    def load_to_widgets(self, data: dict) -> None:
        self.set_text_widget_content(self.text_otd, content=data['otd'])
        self.set_text_widget_content(self.text_feat_article, content=data['featured_article'])

    def get_info(self, url: str) -> None:
        result = self.url_client.get_url_source(url)
        data = dict()
        if result['isSuccess'] is True:
            data = self.wiki_parser.collect_data(result['content'])
        else:
            error_str = 'There is a problem with connection to' + self.url + \
                        '. Error info:' + result['content']
            data['otd'] = error_str
            data['featured_article'] = error_str
        self.load_to_widgets(data)
