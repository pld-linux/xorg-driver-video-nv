Summary:	X.org video driver for NVIDIA video adapters
Summary(pl):	Sterownik obrazu X.org dla kart graficznych NVIDIA
Name:		xorg-driver-video-nv
Version:	1.0.1.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-video-nv-%{version}.tar.bz2
# Source0-md5:	696d16ea4390be27cb2654377347dfb7
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for NVIDIA video adapters. It supports PCI and AGP
video cards based on the following chips: RIVA 128 (NV3), RIVA TNT
(NV4), GeForce 256, QUADRO (NV10), GeForce2, QUADRO2 (NV11, NV15),
GeForce3, QUADRO DCC (NV20), nForce, nForce2 (NV1A, NV1F), GeForce4,
QUADRO4 (NV17, NV18, NV25, NV28), GeForce FX, QUADRO FX (NV30, NV31,
NV34, NV35, NV36, NV37, NV38), GeForce 6xxx (NV40, NV41, NV43, NV44,
NV45), GeForce 7xxx (G70).

%description -l pl
Sterownik obrazu X.org dla kart graficznych NVIDIA. Obs³uguje karty
PCI i AGP oparte na nastêpuj±cych uk³adach: RIVA 128 (NV3), RIVA TNT
(NV4), GeForce 256, QUADRO (NV10), GeForce2, QUADRO2 (NV11, NV15),
GeForce3, QUADRO DCC (NV20), nForce, nForce2 (NV1A, NV1F), GeForce4,
QUADRO4 (NV17, NV18, NV25, NV28), GeForce FX, QUADRO FX (NV30, NV31,
NV34, NV35, NV36, NV37, NV38), GeForce 6xxx (NV40, NV41, NV43, NV44,
NV45), GeForce 7xxx (G70).

%prep
%setup -q -n xf86-video-nv-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.NV1
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/nv_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/riva128.so
%{_mandir}/man4/nv.4x*
