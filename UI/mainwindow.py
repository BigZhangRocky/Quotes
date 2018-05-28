# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './res/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1482, 931)
        MainWindow.setDocumentMode(True)
        self.central_widget_ = QtWidgets.QWidget(MainWindow)
        self.central_widget_.setObjectName("central_widget_")
        self.mdi_area_ = QtWidgets.QMdiArea(self.central_widget_)
        self.mdi_area_.setGeometry(QtCore.QRect(0, 0, 1491, 851))
        self.mdi_area_.setObjectName("mdi_area_")
        MainWindow.setCentralWidget(self.central_widget_)
        self.menu_bar_ = QtWidgets.QMenuBar(MainWindow)
        self.menu_bar_.setGeometry(QtCore.QRect(0, 0, 1482, 23))
        self.menu_bar_.setDefaultUp(False)
        self.menu_bar_.setObjectName("menu_bar_")
        self.file_menu_ = QtWidgets.QMenu(self.menu_bar_)
        self.file_menu_.setObjectName("file_menu_")
        self.edit_menu_ = QtWidgets.QMenu(self.menu_bar_)
        self.edit_menu_.setObjectName("edit_menu_")
        self.view_menu_ = QtWidgets.QMenu(self.menu_bar_)
        self.view_menu_.setObjectName("view_menu_")
        self.windows_menu_ = QtWidgets.QMenu(self.menu_bar_)
        self.windows_menu_.setObjectName("windows_menu_")
        MainWindow.setMenuBar(self.menu_bar_)
        self.status_bar_ = QtWidgets.QStatusBar(MainWindow)
        self.status_bar_.setObjectName("status_bar_")
        MainWindow.setStatusBar(self.status_bar_)
        self.tool_bar_ = QtWidgets.QToolBar(MainWindow)
        self.tool_bar_.setAllowedAreas(QtCore.Qt.LeftToolBarArea|QtCore.Qt.RightToolBarArea)
        self.tool_bar_.setOrientation(QtCore.Qt.Horizontal)
        self.tool_bar_.setObjectName("tool_bar_")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.tool_bar_)
        self.draw_panel_ = QtWidgets.QToolBar(MainWindow)
        self.draw_panel_.setOrientation(QtCore.Qt.Horizontal)
        self.draw_panel_.setObjectName("draw_panel_")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.draw_panel_)
        MainWindow.insertToolBarBreak(self.draw_panel_)
        self.stock_list_1 = QtWidgets.QDockWidget(MainWindow)
        self.stock_list_1.setObjectName("stock_list_1")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.stock_list_1.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.stock_list_1)
        self.actionSelect_Data_Source = QtWidgets.QAction(MainWindow)
        self.actionSelect_Data_Source.setCheckable(True)
        self.actionSelect_Data_Source.setObjectName("actionSelect_Data_Source")
        self.action_kline_1m_ = QtWidgets.QAction(MainWindow)
        self.action_kline_1m_.setCheckable(True)
        self.action_kline_1m_.setObjectName("action_kline_1m_")
        self.action_kline_5m_ = QtWidgets.QAction(MainWindow)
        self.action_kline_5m_.setCheckable(True)
        self.action_kline_5m_.setObjectName("action_kline_5m_")
        self.action_kline_30m_ = QtWidgets.QAction(MainWindow)
        self.action_kline_30m_.setCheckable(True)
        self.action_kline_30m_.setObjectName("action_kline_30m_")
        self.action_kline_days_ = QtWidgets.QAction(MainWindow)
        self.action_kline_days_.setCheckable(True)
        self.action_kline_days_.setObjectName("action_kline_days_")
        self.action_kline_week_ = QtWidgets.QAction(MainWindow)
        self.action_kline_week_.setCheckable(True)
        self.action_kline_week_.setObjectName("action_kline_week_")
        self.action_kline_month_ = QtWidgets.QAction(MainWindow)
        self.action_kline_month_.setCheckable(True)
        self.action_kline_month_.setObjectName("action_kline_month_")
        self.action_kline_season_ = QtWidgets.QAction(MainWindow)
        self.action_kline_season_.setCheckable(True)
        self.action_kline_season_.setObjectName("action_kline_season_")
        self.action_kline_year_ = QtWidgets.QAction(MainWindow)
        self.action_kline_year_.setCheckable(True)
        self.action_kline_year_.setObjectName("action_kline_year_")
        self.action_save_cur_winlayout_ = QtWidgets.QAction(MainWindow)
        self.action_save_cur_winlayout_.setObjectName("action_save_cur_winlayout_")
        self.action_hide_stock_list_ = QtWidgets.QAction(MainWindow)
        self.action_hide_stock_list_.setObjectName("action_hide_stock_list_")
        self.action_restore_pre_vwinlayout_ = QtWidgets.QAction(MainWindow)
        self.action_restore_pre_vwinlayout_.setObjectName("action_restore_pre_vwinlayout_")
        self.file_menu_.addAction(self.actionSelect_Data_Source)
        self.view_menu_.addAction(self.action_kline_1m_)
        self.view_menu_.addAction(self.action_kline_5m_)
        self.view_menu_.addAction(self.action_kline_30m_)
        self.view_menu_.addAction(self.action_kline_days_)
        self.view_menu_.addAction(self.action_kline_week_)
        self.view_menu_.addAction(self.action_kline_month_)
        self.view_menu_.addAction(self.action_kline_season_)
        self.view_menu_.addAction(self.action_kline_year_)
        self.windows_menu_.addAction(self.action_save_cur_winlayout_)
        self.windows_menu_.addAction(self.action_restore_pre_vwinlayout_)
        self.windows_menu_.addSeparator()
        self.windows_menu_.addAction(self.action_hide_stock_list_)
        self.menu_bar_.addAction(self.file_menu_.menuAction())
        self.menu_bar_.addAction(self.edit_menu_.menuAction())
        self.menu_bar_.addAction(self.view_menu_.menuAction())
        self.menu_bar_.addAction(self.windows_menu_.menuAction())
        self.tool_bar_.addAction(self.action_hide_stock_list_)
        self.tool_bar_.addSeparator()
        self.tool_bar_.addAction(self.action_kline_1m_)
        self.tool_bar_.addAction(self.action_kline_5m_)
        self.tool_bar_.addAction(self.action_kline_30m_)
        self.tool_bar_.addAction(self.action_kline_days_)
        self.tool_bar_.addAction(self.action_kline_week_)
        self.tool_bar_.addAction(self.action_kline_month_)
        self.tool_bar_.addAction(self.action_kline_season_)
        self.tool_bar_.addAction(self.action_kline_year_)
        self.tool_bar_.addSeparator()
        self.tool_bar_.addAction(self.action_restore_pre_vwinlayout_)
        self.tool_bar_.addAction(self.action_save_cur_winlayout_)
        self.tool_bar_.addSeparator()
        self.draw_panel_.addSeparator()

        self.retranslateUi(MainWindow)
        self.action_kline_1m_.triggered['bool'].connect(MainWindow.onKLineChanged)
        self.action_kline_30m_.triggered['bool'].connect(MainWindow.onKLineChanged)
        self.tool_bar_.actionTriggered['QAction*'].connect(MainWindow.onActionTriggered)
        self.action_restore_pre_vwinlayout_.triggered.connect(MainWindow.onActionRestorePreLayoutTriggered)
        self.action_save_cur_winlayout_.triggered.connect(MainWindow.onActionSaveCurLayoutTriggered)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "缠中说禅量化交易"))
        self.file_menu_.setTitle(_translate("MainWindow", "文件"))
        self.edit_menu_.setTitle(_translate("MainWindow", "编辑"))
        self.view_menu_.setTitle(_translate("MainWindow", "查看"))
        self.windows_menu_.setTitle(_translate("MainWindow", "窗口"))
        self.tool_bar_.setWindowTitle(_translate("MainWindow", "ToolBar"))
        self.draw_panel_.setWindowTitle(_translate("MainWindow", "DrawPanel"))
        self.stock_list_1.setWindowTitle(_translate("MainWindow", "股票列表"))
        self.actionSelect_Data_Source.setText(_translate("MainWindow", "Select Data Source"))
        self.action_kline_1m_.setText(_translate("MainWindow", "1分钟"))
        self.action_kline_5m_.setText(_translate("MainWindow", "5分钟"))
        self.action_kline_30m_.setText(_translate("MainWindow", "30分钟"))
        self.action_kline_days_.setText(_translate("MainWindow", "日线"))
        self.action_kline_week_.setText(_translate("MainWindow", "周线"))
        self.action_kline_month_.setText(_translate("MainWindow", "月线"))
        self.action_kline_season_.setText(_translate("MainWindow", "季线"))
        self.action_kline_year_.setText(_translate("MainWindow", "年线"))
        self.action_save_cur_winlayout_.setText(_translate("MainWindow", "保存当前布局"))
        self.action_hide_stock_list_.setText(_translate("MainWindow", "隐藏股票列表"))
        self.action_restore_pre_vwinlayout_.setText(_translate("MainWindow", "恢复上一布局"))

