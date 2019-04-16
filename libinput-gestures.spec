Summary:        libinput gestures
Name:           libinput-gestures
Version:        2.42
Release:        1%{?dist}

License:        GNU
URL:            https://github.com/bulletmark/%{name}

BuildArch:      noarch

Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Requires: xdotool
Requires: wmctrl

#BuildRequires: make
BuildRequires: desktop-file-utils

%description
Libinput-gestures is a utility which reads libinput gestures from your touchpad and maps them to gestures you configure in a configuration file. Each gesture can be configured to activate a shell command which is typically an xdotool command to action desktop/window/application keyboard combinations and commands.

%prep
%autosetup -n %{name}-%{version} -p1

%install
# Installing executables...
%{__mkdir_p} "%{buildroot}%{_bindir}"
%{__install} -m 0755 -p %{name} "%{buildroot}%{_bindir}/%{name}"
%{__install} -m 0755 -p %{name}-setup "%{buildroot}%{_bindir}/%{name}-setup"

# Installing desktop shortcut...
desktop-file-install --dir="%{buildroot}%{_datadir}/applications" %{name}.desktop

# Installing icon...
dir="%{buildroot}%{_datadir}/icons/hicolor/128x128/apps"
%{__install} -d "$dir"
%{__install} -m 0644 -p %{name}.png "$dir/%{name}.png"

# Installing configuration file...
dir="%{buildroot}%{_sysconfdir}"
%{__install} -d "$dir"
%{__install} -m 0644 -p %{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf
#install -CDv -m 0644 -t $DESTDIR$DOCDIR README.md

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
* Tue Apr 16 2019 Michael Hrechyn
- Initial package
