%define name cdparanoia-plugin
%define version 0.1
%define release %mkrel 12

Summary: Digital CD playback plugin for XMMS
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
URL: http://www02.u-page.so-net.ne.jp/ca2/kzmi/xmms/
License: GPLv2+
Group: Sound
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libxmms-devel
BuildRequires: libcdda-devel
BuildRequires: automake1.4
Requires: xmms

%description
This plugin reads CDDA sectors and passes them to XMMS directly. That
way you don't need a cable from the CD-ROM to the sound card and you
can use the usual effect and visualization plugins.

%prep
%setup -q
aclocal-1.4
autoconf
automake-1.4 --foreign
libtoolize --force

%build
export LDFLAGS=-lm
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/xmms/Input/libcdparanoia.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%_libdir/xmms/Input/libcdparanoia.so


