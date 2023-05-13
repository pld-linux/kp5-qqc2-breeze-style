#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.27.5
%define		qtver		5.15.2
%define		kpname		qqc2-breeze-style

Summary:	QQC2StyleBridge
Name:		kp5-%{kpname}
Version:	5.27.5
Release:	3
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	6bc2603e9b50728639a0274ed108ebf1
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Quick-controls2-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
This is a pure Qt Quick/Kirigami Qt Quick Controls style. Unlike
QQC2-Desktop-Style, it does not depend on Qt Widgets and the system
QStyle. It looks like the KDE Visual Design Group's vision for Breeze.

It behaves similar to how the Qt Basic, Fusion and Material QQC2
styles behave, but with various extra features to improve the user
experience.

The performance, loading times and RAM usage should be generally
competitive with the Qt Fusion and Material QQC2 styles.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/cmake/KF5QQC2BreezeStyle
%{_libdir}/cmake/KF5QQC2BreezeStyle/KF5QQC2BreezeStyleConfig.cmake
%{_libdir}/cmake/KF5QQC2BreezeStyle/KF5QQC2BreezeStyleConfigVersion.cmake
%{_libdir}/qt5/plugins/kf5/kirigami/org.kde.breeze.so
%dir %{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/AbstractButton.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/ApplicationWindow.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/BusyIndicator.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/Button.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/ButtonGroup.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/CheckBox.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/CheckDelegate.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/ComboBox.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/Container.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/Control.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/DelayButton.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/Dial.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/Dialog.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/DialogButtonBox.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/Drawer.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/Frame.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/GroupBox.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/HorizontalHeaderView.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/ItemDelegate.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/Label.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/Menu.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/MenuBar.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/MenuBarItem.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/MenuItem.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/MenuSeparator.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/MobileTextActionsToolBar.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/Page.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/PageIndicator.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/Pane.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/Popup.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/ProgressBar.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/RadioButton.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/RadioDelegate.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/RangeSlider.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/RoundButton.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/ScrollBar.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/ScrollIndicator.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/ScrollView.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/Slider.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/SpinBox.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/SplitView.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/StackView.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/SwipeDelegate.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/SwipeView.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/Switch.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/SwitchDelegate.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/TabBar.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/TabButton.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/TextArea.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/TextField.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/ToolBar.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/ToolButton.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/ToolSeparator.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/ToolTip.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/Tumbler.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/VerticalHeaderView.qml
%dir %{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/ButtonBackground.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/CheckIndicator.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/ComboBoxBackground.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/CursorDelegate.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/CursorHandle.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/DelegateBackground.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/FocusRect.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/IconLabelContent.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/IconLabelShortcutContent.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/InlineIconLabelContent.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/LargeShadow.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/ListViewHighlight.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/MediumShadow.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/MenuItemBackground.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/OverlayDimBackground.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/OverlayModalBackground.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/RadioIndicator.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/ScrollHandle.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/SliderGroove.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/SliderHandle.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/SpinBoxIndicator.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/SwitchIndicator.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/TextEditBackground.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/qmldir
%dir %{_libdir}/qt5/qml/org/kde/breeze
%dir %{_libdir}/qt5/qml/org/kde/breeze/impl
%{_libdir}/qt5/qml/org/kde/breeze/impl/ButtonBackground.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/CheckIndicator.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/ComboBoxBackground.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/CursorDelegate.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/CursorHandle.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/DelegateBackground.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/FocusRect.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/IconLabelContent.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/IconLabelShortcutContent.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/InlineIconLabelContent.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/LargeShadow.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/ListViewHighlight.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/MediumShadow.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/MenuItemBackground.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/OverlayDimBackground.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/OverlayModalBackground.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/RadioIndicator.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/ScrollHandle.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/SliderGroove.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/SliderHandle.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/SpinBoxIndicator.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/SwitchIndicator.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/TextEditBackground.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/qmldir
%{_libdir}/qt5/qml/org/kde/breeze/libqqc2breezestyleplugin.so
%{_libdir}/qt5/qml/org/kde/breeze/qmldir
%dir %{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/AbstractApplicationHeader.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/AbstractListItem.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/Separator.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/SwipeListItem.qml
%dir %{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/ButtonBackground.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/CheckIndicator.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/ComboBoxBackground.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/CursorDelegate.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/CursorHandle.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/DelegateBackground.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/FocusRect.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/IconLabelContent.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/IconLabelShortcutContent.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/InlineIconLabelContent.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/LargeShadow.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/ListViewHighlight.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/MediumShadow.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/MenuItemBackground.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/OverlayDimBackground.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/OverlayModalBackground.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/RadioIndicator.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/ScrollHandle.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/SliderGroove.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/SliderHandle.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/SpinBoxIndicator.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/SwitchIndicator.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/TextEditBackground.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/Units.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/qmldir
%{_libdir}/qt5/qml/org/kde/breeze/impl/Units.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/Units.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/qmldir
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze/impl/SmallBoxShadow.qml
%{_libdir}/qt5/qml/org/kde/breeze/impl/SmallBoxShadow.qml
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze/impl/SmallBoxShadow.qml
