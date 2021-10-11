%global srcname gestures

Name:           python3-%{srcname}
Version:        0.2.6
Release:        1%{?dist}
Summary:        A minimal Gtk+ GUI app for libinput-gestures

License:        GPLv3
URL:            https://gitlab.com/cunidev/gestures
Source0:        %{url}/-/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gtk3
BuildRequires:  python3-devel
BuildRequires:  python3-gobject

Requires:       gtk3
Requires:       libinput-gestures
Requires:       python3-gobject

%description
A minimal Gtk+ GUI app for libinput-gestures.


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files
%doc README.md
%license LICENSE
%{_bindir}/%{srcname}
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.cunidev.%{srcname}.svg
%{_metainfodir}/*.xml


%changelog
* Mon Oct 11 2021 Chris Cowley <chris@cowley.tech> - 0.2.6-1
- Update to version 0.2.6

* Sat Nov 14 08:22:32 +03 2020 ElXreno <elxreno@gmail.com> - 0.2.3-1
- Update to version 0.2.3

* Mon Mar  9 2020 ElXreno <elxreno@gmail.com>
- Initial packaging
