Name:           libinput-gestures
Version:        2.42
Release:        4%{?dist}

Summary:        Actions gestures on your touchpad using libinput

License:        GPLv3+
URL:            https://github.com/bulletmark/libinput-gestures
Source0:        %{url}/archive/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  make

Requires:       python3 >= 3.4
Requires:       hicolor-icon-theme
Requires:       wmctrl
Requires:       xdotool

%description
Libinput-gestures is a utility which reads libinput gestures from your touchpad
and maps them to gestures you configure in a configuration file. Each gesture
can be configured to activate a shell command which is typically an xdotool
command to action desktop/window/application keyboard combinations and commands.

%prep
%autosetup

%install
%make_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
echo "Add users to 'input' group, if it needed"
echo "Add libinput-gestures to autostart by typing 'libinput-gestures-setup autostart', if it needed"
echo "Run libinput-gestures by typing 'libinput-gestures-setup start'"

%files
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-setup
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_sysconfdir}/%{name}.conf

%changelog
* Thu Apr 18 2019 Michael Hrechyn <elxreno@gmail.com> - 2.42-4
- Merge spec file from another spec

* Thu Apr 18 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.42-3
- Update spec file

* Wed Apr 17 2019 Michael Hrechyn - 2.42-2
- Now the installation past through make install

* Tue Apr 16 2019 Michael Hrechyn
- Initial package
