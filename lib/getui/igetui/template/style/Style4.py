from .AbstractNotifyStyle import *
from protobuf.gt_req_pb2 import InnerFiled

class Style4(AbstractNotifyStyle):
    def __init__(self):
        AbstractNotifyStyle.__init__(self)
        self.logo = ""
        self.banner_url = ""

    def getActionChain(self):
        title_F = self.actionChainBuilder.field.add()
        title_F.key = "logo"
        title_F.val = self.logo
        title_F.type = InnerFiled.str

        banner_url_F = self.actionChainBuilder.field.add()
        banner_url_F.key = "banner_url"
        banner_url_F.val = self.banner_url
        banner_url_F.type = InnerFiled.str

        isRing_F = self.actionChainBuilder.field.add()
        isRing_F.key = "is_noring"
        isRing_F.val = str(False if self.isRing else True)
        isRing_F.type = InnerFiled.bool

        isClearable_F = self.actionChainBuilder.field.add()
        isClearable_F.key = "isClearable"
        isClearable_F.val = str(False if self.isClearable else True)
        isClearable_F.type = InnerFiled.bool

        isVibrate_F = self.actionChainBuilder.field.add()
        isVibrate_F.key = "is_noclear"
        isVibrate_F.val = str(False if self.isVibrate else True)
        isVibrate_F.type = InnerFiled.bool

        notifyStyle_F = self.actionChainBuilder.field.add()
        notifyStyle_F.key = "notifyStyle"
        notifyStyle_F.val = "4"
        notifyStyle_F.type = InnerFiled.str
        return self.actionChainBuilder