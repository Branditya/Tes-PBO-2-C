# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"192410101082", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Dandy Wiraditya Putra", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"HELLO WX", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 22, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Black" ) )

		bSizer3.Add( self.m_staticText7, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


