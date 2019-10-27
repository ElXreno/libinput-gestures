Name:           libinput-gestures
Version:        2.48
Release:        1%{?dist}

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
if [ $1 -gt 1 ] ; then
    echo "You must add yourself to input group and re-login (or reboot) before using this program. Execute \"sudo usermod -aG input $(whoami)\""
    echo "Add service to autostart (if required): \"libinput-gestures-setup autostart\""
    echo "Start service: \"libinput-gestures-setup start\""
fi

%files
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-setup
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%config(noreplace) %{_sysconfdir}/%{name}.conf

%changelog
* Sun Oct 27 2019 ElXreno <elxreno@gmail.com> - 2.48-1
- Bump to 2.48 version

* Sat Oct 19 2019 ElXreno <elxreno@gmail.com> - 2.47-1
- Bump to 2.47 version and update post hook

* Sat Jul 27 2019 ElXreno <elxreno@gmail.com> - 2.45-1
- Bump to 2.45 version

* Thu Apr 18 2019 ElXreno <elxreno@gmail.com> - 2.42-4
- Merge spec file from another spec

* Thu Apr 18 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.42-3
- Update spec file

* Wed Apr 17 2019 ElXreno <elxreno@gmail.com> - 2.42-2
- Now the installation past through make install

* Tue Apr 16 2019 ElXreno <elxreno@gmail.com> - 2.42-1
- Initial package
