Name: koffice-l10n-cs
Version: 2.0.82
Release: %mkrel 2
Summary: Language files for KOffice Czech
Group: System/Internationalization
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv2+
URL: https://www.koffice.org
BuildArch: noarch
Source: ftp://ftp.kde.org/pub/kde/stable/koffice-%version/src/koffice-l10n/%name-%version.tar.bz2
BuildRequires: gettext >= 0.15
BuildRequires: kdelibs4-devel
Requires: locales-cs
Requires: koffice-core
Provides: koffice-l10n

%description 
Provides Czech translations for KOffice.

%files 
%defattr(-,root,root,-)
%{_kde_datadir}/*/*/*

#------------------------------------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.82-2mdv2011.0
+ Revision: 612632
- the mass rebuild of 2010.1 packages

* Thu Sep 17 2009 Funda Wang <fwang@mandriva.org> 2.0.82-1mdv2010.0
+ Revision: 443735
- new version 2.0.82

* Wed Aug 12 2009 Funda Wang <fwang@mandriva.org> 2.0.2-1mdv2010.0
+ Revision: 415388
- new version 2.0.2

* Sat Jun 27 2009 Funda Wang <fwang@mandriva.org> 2.0.1-1mdv2010.0
+ Revision: 389641
- new version 2.0.1

* Thu May 28 2009 Funda Wang <fwang@mandriva.org> 2.0.0-1mdv2010.0
+ Revision: 380396
- import koffice-l10n-cs


