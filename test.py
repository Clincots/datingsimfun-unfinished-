import time
import asyncio
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.screenmanager import FadeTransition
from kivy.clock import Clock
from kivy.animation import Animation

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

Builder.load_file("test.kv")

affinity = 50
class whitescreen(Screen):
    pass
class blackscreen(Screen):
    pass
class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class ThirdScreen(Screen):
    pass


class FourthScreen(Screen):
    pass

class Five(Screen):
    pass
    def checkafi(self):
        if affinity >= 40:
            self.manager.current = 'winner'
        else:
            self.manager.current = 'loer'

class Six(Screen):
    pass

class Seven(Screen):
    pass

class Eight(Screen):
    def gowhite(self, *args):
        Clock.schedule_once(self.next2, .00001)
        Clock.schedule_once(self.next3, .00002)
        Clock.schedule_once(self.next4, .5)

    def next2(self, dt):
        self.manager.current = "eighth"
    def next3(self, dt):
        self.manager.current = "whitescreen"
    def next4(self, dt):
        self.manager.current = "ninth"

class Nine(Screen):
    pass

class Ten(Screen):
    pass

class Eleven(Screen):
    def giveelevenaffinity(self):
        global affinity
        affinity += 10

class Twelve(Screen):
    pass

class Thirteen(Screen):
    def funny(self, *args):
        Clock.schedule_once(self.next_screen, .00001)
        Clock.schedule_once(self.next_screen4, .025)
        Clock.schedule_once(self.next_screen5, .05)
        Clock.schedule_once(self.next_screen6, .075)
        Clock.schedule_once(self.next_screen7, .1)
        Clock.schedule_once(self.next_screen8, .125)
        Clock.schedule_once(self.next_screen9, .15)
        Clock.schedule_once(self.next_screen10, .175)
        Clock.schedule_once(self.next_screen11, .2)
        Clock.schedule_once(self.next_screen12, .225)
        Clock.schedule_once(self.next_screen13, .25)
        Clock.schedule_once(self.next_screen14, .275)
        Clock.schedule_once(self.next_screen15, .3)
        Clock.schedule_once(self.next_screen16, .325)
        Clock.schedule_once(self.next_screen17, .35)
        Clock.schedule_once(self.next_screen18, .375)
        Clock.schedule_once(self.next_screen19, .4)
        Clock.schedule_once(self.next_screen20, .425)
        Clock.schedule_once(self.next_screen21, .525)
        Clock.schedule_once(self.next_screen22, .55)
        Clock.schedule_once(self.next_screen23, .575)
        Clock.schedule_once(self.next_screen24, .6)
        Clock.schedule_once(self.next_screen25, .625)
        Clock.schedule_once(self.next_screen26, .65)
        Clock.schedule_once(self.next_screen27, .675)
        Clock.schedule_once(self.next_screen28, .7)
        Clock.schedule_once(self.next_screen29, .725)
        Clock.schedule_once(self.next_screen30, .75)
        Clock.schedule_once(self.next_screen31, .775)
        Clock.schedule_once(self.next_screen32, .8)
        Clock.schedule_once(self.next_screen32, .825)
        Clock.schedule_once(self.next_screen34, .85)
        Clock.schedule_once(self.next_screen35, .875)
        Clock.schedule_once(self.next_screen36, .9)
        Clock.schedule_once(self.next_screen37, .925)
        Clock.schedule_once(self.next_screen38, .95)
        Clock.schedule_once(self.next_screen39, .975)
        Clock.schedule_once(self.next_screen40, 1)
        Clock.schedule_once(self.next_screen2, 1.025) #no circle
        Clock.schedule_once(self.next_screen3, 1.4) #siwtch text

    def next_screen(self, dt):
        self.manager.current = "fifteenth"

    def next_screen4(self, dt):
        self.manager.current = "a17"

    def next_screen5(self, dt):
        self.manager.current = "a18"

    def next_screen6(self, dt):
        self.manager.current = "a19"

    def next_screen7(self, dt):
        self.manager.current = "a20"
    def next_screen40(self, dt):
        self.manager.current = "a56"
    def next_screen8(self, dt):
        self.manager.current = "a22"
    def next_screen9(self, dt):
        self.manager.current = "a23"
    def next_screen10(self, dt):
        self.manager.current = "a24"
    def next_screen11(self, dt):
        self.manager.current = "a25"
    def next_screen12(self, dt):
        self.manager.current = "a26"
    def next_screen13(self, dt):
        self.manager.current = "a27"
    def next_screen14(self, dt):
        self.manager.current = "a28"
    def next_screen15(self, dt):
        self.manager.current = "a29"
    def next_screen16(self, dt):
        self.manager.current = "a30"
    def next_screen17(self, dt):
        self.manager.current = "a31"
    def next_screen18(self, dt):
        self.manager.current = "a32"
    def next_screen19(self, dt):
        self.manager.current = "a33"
    def next_screen20(self, dt):
        self.manager.current = "a34"
    def next_screen21(self, dt):
        self.manager.current = "a35"
    def next_screen22(self, dt):
        self.manager.current = "a36"
    def next_screen23(self, dt):
        self.manager.current = "a37"
    def next_screen24(self, dt):
        self.manager.current = "a38"
    def next_screen25(self, dt):
        self.manager.current = "a39"
    def next_screen26(self, dt):
        self.manager.current = "a40"
    def next_screen27(self, dt):
        self.manager.current = "a41"
    def next_screen28(self, dt):
        self.manager.current = "a42"
    def next_screen29(self, dt):
        self.manager.current = "a43"
    def next_screen30(self, dt):
        self.manager.current = "a44"
    def next_screen31(self, dt):
        self.manager.current = "a45"
    def next_screen32(self, dt):
        self.manager.current = "a46"
    def next_screen33(self, dt):
        self.manager.current = "a47"
    def next_screen34(self, dt):
        self.manager.current = "a48"
    def next_screen35(self, dt):
        self.manager.current = "a49"
    def next_screen36(self, dt):
        self.manager.current = "a50"
    def next_screen37(self, dt):
        self.manager.current = "a51"
    def next_screen38(self, dt):
        self.manager.current = "a52"
    def next_screen39(self, dt):
        self.manager.current = "a53"
    def next_screen2(self, dt):
        self.manager.current = "sixteenth"

    def next_screen3(self, dt):
        self.manager.current = "fourteenth"

class Fourteen(Screen):
    pass

class Fifteen(Screen):
    pass

class Sixteen(Screen):
    pass

class winner(Screen):
    pass

class loer(Screen):
    pass

class a17(Screen):
    pass

class a18(Screen):
    pass

class a19(Screen):
    pass

class a20(Screen):
    pass

class a21(Screen):
    pass

class a22(Screen):
    pass

class a23(Screen):
    pass

class a24(Screen):
    pass

class a25(Screen):
    pass

class a26(Screen):
    pass

class a27(Screen):
    pass

class a28(Screen):
    pass

class a29(Screen):
    pass

class a30(Screen):
    pass

class a31(Screen):
    pass

class a32(Screen):
    pass

class a33(Screen):
    pass

class a34(Screen):
    pass

class a35(Screen):
    pass

class a36(Screen):
    pass

class a37(Screen):
    pass

class a38(Screen):
    pass

class a39(Screen):
    pass

class a40(Screen):
    pass

class a41(Screen):
    pass

class a42(Screen):
    pass

class a43(Screen):
    pass

class a44(Screen):
    pass

class a45(Screen):
    pass

class a46(Screen):
    pass

class a47(Screen):
    pass

class a48(Screen):
    pass

class a49(Screen):
    pass

class a50(Screen):
    pass

class a51(Screen):
    pass

class a52(Screen):
    pass

class a53(Screen):
    pass

class a54(Screen):
    pass

class a55(Screen):
    def funy2(self, *args):
        Clock.schedule_once(self.next3, .0001)
        Clock.schedule_once(self.next4, .5)
        Clock.schedule_once(self.next5, 1)


    def next3(self, dt):
        #blur here
        self.manager.current = "blackscreen"
        #blur here


    def next4(self, dt):
        self.manager.current = "a58"

    def next5(self, dt):    
        self.manager.current = "a60"

class a56(Screen):
    pass

class a57(Screen):
    def afficheckyes(self):
        global affinity
        if affinity >= 60:
            self.manager.transition = FadeTransition()
            self.manager.current = "a59"
            self.manager.transition = FadeTransition()

        else:
            self.manager.current = "a55"

class a58(Screen):
    pass

class a59(Screen):
    def check(self):
        print(self.manager.transition)

class a60(Screen):
    pass

class a61(Screen):
    pass

class a62(Screen):
    def on_enter(self, *args):
        Clock.schedule_once(self.next3, .025)
        Clock.schedule_once(self.next4, .05)
        Clock.schedule_once(self.next5, .075)
        Clock.schedule_once(self.next6, .1)
        Clock.schedule_once(self.next7, .125)
        Clock.schedule_once(self.next8, .15)
        Clock.schedule_once(self.next9, .175)
        Clock.schedule_once(self.next10, .2)
        Clock.schedule_once(self.next11, .225)
        Clock.schedule_once(self.next12, .25)
        Clock.schedule_once(self.next13, .275)
        Clock.schedule_once(self.next14, .3)
        Clock.schedule_once(self.next15, .325)
        Clock.schedule_once(self.next16, .35)
        Clock.schedule_once(self.next17, .375)



    def next3(self, dt):
        # blur here
        self.manager.current = "a63"
        # blur here

    def next4(self, dt):
        self.manager.current = "a64"

    def next5(self, dt):
        self.manager.current = "a65"

    def next6(self, dt):
        self.manager.current = "a66"

    def next7(self, dt):
        self.manager.current = "a67"

    def next8(self, dt):
        self.manager.current = "a68"
    def next9(self, dt):
        self.manager.current = "a69"
    def next10(self, dt):
        self.manager.current = "a70"
    def next11(self, dt):
        self.manager.current = "a71"
    def next12(self, dt):
        self.manager.current = "a72"
    def next13(self, dt):
        self.manager.current = "a73"
    def next14(self, dt):
        self.manager.current = "a74"
    def next15(self, dt):
        self.manager.current = "a75"
    def next16(self, dt):
        self.manager.current = "a76"
    def next17(self, dt):
        print(crash)


class a63(Screen):
    pass

class a64(Screen):
    pass

class a65(Screen):
    pass

class a66(Screen):
    pass

class a67(Screen):
    pass

class a68(Screen):
    pass

class a69(Screen):
    pass

class a70(Screen):
    pass

class a71(Screen):
    pass

class a72(Screen):
    pass

class a73(Screen):
    pass

class a74(Screen):
    pass

class a75(Screen):
    pass

class a76(Screen):
    pass

class a77(Screen):
    pass

class a78(Screen):
    pass

class a79(Screen):
    pass

class a80(Screen):
    pass

class a81(Screen):
    pass

class a82(Screen):
    pass

class a83(Screen):
    pass

class a84(Screen):
    pass

class a85(Screen):
    pass

class a86(Screen):
    pass

class a87(Screen):
    pass

class a88(Screen):
    pass

class a89(Screen):
    pass
class a90(Screen):
    pass
class a91(Screen):
    pass
class a92(Screen):
    pass
class a93(Screen):
    pass
class a94(Screen):
    pass
class a95(Screen):
    pass
class a96(Screen):
    pass
class a97(Screen):
    pass
class a98(Screen):
    pass
class a99(Screen):
    pass
class a100(Screen):
    pass
class a101(Screen):
    pass
class a102(Screen):
    pass
class a103(Screen):
    pass
class a104(Screen):
    pass
class a105(Screen):
    pass
class a106(Screen):
    pass
class a107(Screen):
    pass
class a108(Screen):
    pass
class a109(Screen):
    pass
class a110(Screen):
    pass
class a111(Screen):
    pass
class a112(Screen):
    pass
class a113(Screen):
    pass
class a114(Screen):
    pass
class a115(Screen):
    pass
class a116(Screen):
    pass
class a117(Screen):
    pass
class a118(Screen):
    pass
class a119(Screen):
    pass
class a120(Screen):
    pass
class a121(Screen):
    pass
class a122(Screen):
    pass
class a123(Screen):
    pass
class a124(Screen):
    pass
class a125(Screen):
    pass
class a126(Screen):
    pass
class a127(Screen):
    pass
class a128(Screen):
    pass
class a129(Screen):
    pass
class a130(Screen):
    pass
class a131(Screen):
    pass
class a132(Screen):
    pass
class a133(Screen):
    pass
class a134(Screen):
    pass
class a135(Screen):
    pass
class a136(Screen):
    pass
class a137(Screen):
    pass
class a138(Screen):
    pass
class a139(Screen):
    pass
class a140(Screen):
    pass
class a141(Screen):
    pass
class a142(Screen):
    pass
class a143(Screen):
    pass
class a144(Screen):
    pass
class a145(Screen):
    pass
class a146(Screen):
    pass
class a147(Screen):
    pass
class a148(Screen):
    pass
class a149(Screen):
    pass
class a150(Screen):
    pass
class a151(Screen):
    pass
class a152(Screen):
    pass
class a153(Screen):
    pass
class a154(Screen):
    pass
class a155(Screen):
    pass
class a156(Screen):
    pass
class a157(Screen):
    pass
class a158(Screen):
    pass
class a159(Screen):
    pass
class a160(Screen):
    pass
class a161(Screen):
    pass
class a162(Screen):
    pass
class a163(Screen):
    pass
class a164(Screen):
    pass
class a165(Screen):
    pass
class a166(Screen):
    pass
class a167(Screen):
    pass
class a168(Screen):
    pass
class a169(Screen):
    pass
class a170(Screen):
    pass
class a171(Screen):
    pass
class a172(Screen):
    pass
class a173(Screen):
    pass
class a174(Screen):
    pass
class a175(Screen):
    pass
class a176(Screen):
    pass
class a177(Screen):
    pass
class a178(Screen):
    pass
class a179(Screen):
    pass
class a180(Screen):
    pass
class a181(Screen):
    pass
class a182(Screen):
    pass
class a183(Screen):
    pass
class a184(Screen):
    pass
class a185(Screen):
    pass
class a186(Screen):
    pass
class a187(Screen):
    pass
class a188(Screen):
    pass
class a189(Screen):
    pass


class CandLApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name="first"))
        sm.add_widget(SecondScreen(name="second"))
        sm.add_widget(ThirdScreen(name="third"))
        sm.add_widget(FourthScreen(name="fourth"))
        sm.add_widget(Five(name="fifth"))
        sm.add_widget(Six(name="sixth"))
        sm.add_widget(Seven(name="seventh"))
        sm.add_widget(Eight(name="eighth"))
        sm.add_widget(Nine(name="ninth"))
        sm.add_widget(Ten(name="tenth"))
        sm.add_widget(Eleven(name="eleventh"))
        sm.add_widget(Twelve(name="twelfth"))
        sm.add_widget(Thirteen(name="thirteenth"))
        sm.add_widget(Fourteen(name="fourteenth"))
        sm.add_widget(Fifteen(name="fifteenth"))
        sm.add_widget(Sixteen(name="sixteenth"))
        sm.add_widget(winner(name="winner"))
        sm.add_widget(loer(name="loer"))
        sm.add_widget(a17(name="a17"))
        sm.add_widget(a18(name="a18"))
        sm.add_widget(a19(name="a19"))
        sm.add_widget(a20(name="a20"))
        sm.add_widget(a21(name="a21"))
        sm.add_widget(a22(name="a22"))
        sm.add_widget(a23(name="a23"))
        sm.add_widget(a24(name="a24"))
        sm.add_widget(a25(name="a25"))
        sm.add_widget(a26(name="a26"))
        sm.add_widget(a27(name="a27"))
        sm.add_widget(a28(name="a28"))
        sm.add_widget(a29(name="a29"))
        sm.add_widget(a30(name="a30"))
        sm.add_widget(a31(name="a31"))
        sm.add_widget(a32(name="a32"))
        sm.add_widget(a33(name="a33"))
        sm.add_widget(a34(name="a34"))
        sm.add_widget(a35(name="a35"))
        sm.add_widget(a36(name="a36"))
        sm.add_widget(a37(name="a37"))
        sm.add_widget(a38(name="a38"))
        sm.add_widget(a39(name="a39"))
        sm.add_widget(a40(name="a40"))
        sm.add_widget(a41(name="a41"))
        sm.add_widget(a42(name="a42"))
        sm.add_widget(a43(name="a43"))
        sm.add_widget(a44(name="a44"))
        sm.add_widget(a45(name="a45"))
        sm.add_widget(a46(name="a46"))
        sm.add_widget(a47(name="a47"))
        sm.add_widget(a48(name="a48"))
        sm.add_widget(a49(name="a49"))
        sm.add_widget(a50(name="a50"))
        sm.add_widget(a51(name="a51"))
        sm.add_widget(a52(name="a52"))
        sm.add_widget(a53(name="a53"))
        sm.add_widget(a54(name="a54"))
        sm.add_widget(a55(name="a55"))
        sm.add_widget(a56(name="a56"))
        sm.add_widget(a57(name="a57"))
        sm.add_widget(a58(name="a58"))
        sm.add_widget(a59(name="a59"))
        sm.add_widget(a60(name="a60"))
        sm.add_widget(a61(name="a61"))
        sm.add_widget(a62(name="a62"))
        sm.add_widget(a63(name="a63"))
        sm.add_widget(a64(name="a64"))
        sm.add_widget(a65(name="a65"))
        sm.add_widget(a66(name="a66"))
        sm.add_widget(a67(name="a67"))
        sm.add_widget(a68(name="a68"))
        sm.add_widget(a69(name="a69"))
        sm.add_widget(a70(name="a70"))
        sm.add_widget(a71(name="a71"))
        sm.add_widget(a72(name="a72"))
        sm.add_widget(a73(name="a73"))
        sm.add_widget(a74(name="a74"))
        sm.add_widget(a75(name="a75"))
        sm.add_widget(a76(name="a76"))
        sm.add_widget(a77(name="a77"))
        sm.add_widget(a78(name="a78"))
        sm.add_widget(a79(name="a79"))
        sm.add_widget(a80(name="a80"))
        sm.add_widget(a81(name="a81"))
        sm.add_widget(a82(name="a82"))
        sm.add_widget(a83(name="a83"))
        sm.add_widget(a84(name="a84"))
        sm.add_widget(a85(name="a85"))
        sm.add_widget(a86(name="a86"))
        sm.add_widget(a87(name="a87"))
        sm.add_widget(a88(name="a88"))
        sm.add_widget(a89(name="a89"))
        sm.add_widget(a90(name="a90"))
        sm.add_widget(a91(name="a91"))
        sm.add_widget(a92(name="a92"))
        sm.add_widget(a93(name="a93"))
        sm.add_widget(a94(name="a94"))
        sm.add_widget(a95(name="a95"))
        sm.add_widget(a96(name="a96"))
        sm.add_widget(a97(name="a97"))
        sm.add_widget(a98(name="a98"))
        sm.add_widget(a99(name="a99"))
        sm.add_widget(a100(name="a100"))
        sm.add_widget(a101(name="a101"))
        sm.add_widget(a102(name="a102"))
        sm.add_widget(a103(name="a103"))
        sm.add_widget(a104(name="a104"))
        sm.add_widget(a105(name="a105"))
        sm.add_widget(a106(name="a106"))
        sm.add_widget(a107(name="a107"))
        sm.add_widget(a108(name="a108"))
        sm.add_widget(a109(name="a109"))
        sm.add_widget(a110(name="a110"))
        sm.add_widget(a111(name="a111"))
        sm.add_widget(a112(name="a112"))
        sm.add_widget(a113(name="a113"))
        sm.add_widget(a114(name="a114"))
        sm.add_widget(a115(name="a115"))
        sm.add_widget(a116(name="a116"))
        sm.add_widget(a117(name="a117"))
        sm.add_widget(a118(name="a118"))
        sm.add_widget(a119(name="a119"))
        sm.add_widget(a120(name="a120"))
        sm.add_widget(a121(name="a121"))
        sm.add_widget(a122(name="a122"))
        sm.add_widget(a123(name="a123"))
        sm.add_widget(a124(name="a124"))
        sm.add_widget(a125(name="a125"))
        sm.add_widget(a126(name="a126"))
        sm.add_widget(a127(name="a127"))
        sm.add_widget(a128(name="a128"))
        sm.add_widget(a129(name="a129"))
        sm.add_widget(a130(name="a130"))
        sm.add_widget(a131(name="a131"))
        sm.add_widget(a132(name="a132"))
        sm.add_widget(a133(name="a133"))
        sm.add_widget(a134(name="a134"))
        sm.add_widget(a135(name="a135"))
        sm.add_widget(a136(name="a136"))
        sm.add_widget(a137(name="a137"))
        sm.add_widget(a138(name="a138"))
        sm.add_widget(a139(name="a139"))
        sm.add_widget(a140(name="a140"))
        sm.add_widget(a141(name="a141"))
        sm.add_widget(a142(name="a142"))
        sm.add_widget(a143(name="a143"))
        sm.add_widget(a144(name="a144"))
        sm.add_widget(a145(name="a145"))
        sm.add_widget(a146(name="a146"))
        sm.add_widget(a147(name="a147"))
        sm.add_widget(a148(name="a148"))
        sm.add_widget(a149(name="a149"))
        sm.add_widget(a150(name="a150"))
        sm.add_widget(a151(name="a151"))
        sm.add_widget(a152(name="a152"))
        sm.add_widget(a153(name="a153"))
        sm.add_widget(a154(name="a154"))
        sm.add_widget(a155(name="a155"))
        sm.add_widget(a156(name="a156"))
        sm.add_widget(a157(name="a157"))
        sm.add_widget(a158(name="a158"))
        sm.add_widget(a159(name="a159"))
        sm.add_widget(a160(name="a160"))
        sm.add_widget(a161(name="a161"))
        sm.add_widget(a162(name="a162"))
        sm.add_widget(a163(name="a163"))
        sm.add_widget(a164(name="a164"))
        sm.add_widget(a165(name="a165"))
        sm.add_widget(a166(name="a166"))
        sm.add_widget(a167(name="a167"))
        sm.add_widget(a168(name="a168"))
        sm.add_widget(a169(name="a169"))
        sm.add_widget(a170(name="a170"))
        sm.add_widget(a171(name="a171"))
        sm.add_widget(a172(name="a172"))
        sm.add_widget(a173(name="a173"))
        sm.add_widget(a174(name="a174"))
        sm.add_widget(a175(name="a175"))
        sm.add_widget(a176(name="a176"))
        sm.add_widget(a177(name="a177"))
        sm.add_widget(a178(name="a178"))
        sm.add_widget(a179(name="a179"))
        sm.add_widget(a180(name="a180"))
        sm.add_widget(a181(name="a181"))
        sm.add_widget(a182(name="a182"))
        sm.add_widget(a183(name="a183"))
        sm.add_widget(a184(name="a184"))
        sm.add_widget(a185(name="a185"))
        sm.add_widget(a186(name="a186"))
        sm.add_widget(a187(name="a187"))
        sm.add_widget(a188(name="a188"))
        sm.add_widget(blackscreen(name="blackscreen"))
        sm.add_widget(whitescreen(name="whitescreen"))

        return sm


    def text_wait(self, text, idforbutton, screennumber):

        anything = getattr(self.root.get_screen(screennumber).ids, idforbutton)
        anything = ""
        Clock.schedule_interval(lambda dt: self.handle_char(iter(text), anything), 1.0)
            #Clock.schedule_once(self.dosmth, 1)

    def handle_char(self, iterator, anything ):
        try:
            anything += next(iterator)
            print(anything)
            return True
        except StopIteration:
            return False

    def fullscreen(self):
        Window.fullscreen = True


    def notfullscreen(self):
        Window.fullscreen = False





if __name__ == "__main__":
    CandLApp().run()
