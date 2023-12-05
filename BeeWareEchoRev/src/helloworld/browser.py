import toga
from toga.style.pack import CENTER, COLUMN, ROW, Pack

# 定义Graze类继承自toga.App
class Graze(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow()

        # 创建WebView组件，设置on_webview_load回调函数，样式为flex=1
        self.webview = toga.WebView(
            on_webview_load=self.on_webview_loaded, style=Pack(flex=1)
        )
        # 创建TextInput组件，初始值为"https://beeware.org/"，样式为flex=1
        self.url_input = toga.TextInput(
            value="https://beeware.org/", style=Pack(flex=1)
        )

        # 创建Box组件，包含两个子组件
        box = toga.Box(
            children=[
                toga.Box(
                    children=[
                        self.url_input,
                        # 创建Button组件，文本为"Go"，点击时调用load_page函数，样式为width=50, padding_left=5
                        toga.Button(
                            "Go",
                            on_press=self.load_page,
                            style=Pack(width=50, padding_left=5),
                        ),
                    ],
                    style=Pack(
                        direction=ROW,
                        alignment=CENTER,
                        padding=5,
                    ),
                ),
                self.webview,
            ],
            style=Pack(direction=COLUMN),
        )

        # 设置主窗口的内容为Box组件
        self.main_window.content = box
        # 将url_input的值赋给WebView的url属性
        self.webview.url = self.url_input.value

        # 显示主窗口
        self.main_window.show()

    # 当点击Button组件时调用load_page函数，将url_input的值赋给WebView的url属性
    def load_page(self, widget):
        self.webview.url = self.url_input.value

    # 当WebView加载完成时调用on_webview_loaded函数，将WebView的url属性赋给url_input的value属性
    def on_webview_loaded(self, widget):
        self.url_input.value = self.webview.url


# 定义主函数
def main():
    # 创建Graze实例，传入应用名称和标识
    return Graze("Graze", "org.beeware.graze")


# 如果作为主程序运行则执行main函数
if __name__ == "__main__":
    # 调用main函数获取Graze实例并执行main_loop方法
    main().main_loop()