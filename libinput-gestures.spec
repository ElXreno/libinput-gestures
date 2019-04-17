Summary:        libinput gestures
Name:           libinput-gestures
Version:        2.42
Release:        2%{?dist}

License:        GNU GPLv3
URL:            https://github.com/bulletmark/libinput-gestures

BuildArch:      noarch

Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Requires: xdotool
Requires: wmctrl

BuildRequires: make
BuildRequires: desktop-file-utils

%description
Libinput-gestures is a utility which reads libinput gestures from your touchpad and maps them to gestures you configure in a configuration file. Each gesture can be configured to activate a shell command which is typically an xdotool command to action desktop/window/application keyboard combinations and commands.

%prep
%autosetup -n %{name}-%{version} -p1

%install
%make_install

%post
echo "Add users to 'input' group, if it needed"
echo "Add libinput-gestures to autostart by typing 'libinput-gestures-setup autostart', if it needed"
echo "Run libinput-gestures by typing 'libinput-gestures-setup start'"

%files
%doc %{_datadir}/doc/%{name}/README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-setup
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_sysconfdir}/%{name}.conf

%changelog
* Wed Apr 17 2019 Michael Hrechyn - 2.42-2
- Now the installation past through make install

* Tue Apr 16 2019 Michael Hrechyn
- Initial package
