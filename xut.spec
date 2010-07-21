#
# TODO: - fix auto tools
#
Summary:	A button football simulation
Summary(hu.UTF-8):	Gombfoci szimuláció
Summary(pl.UTF-8):	Symulator piłki nożnej
Name:		xut
Version:	0.2.1
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/digenv/%{name}-%{version}.tar.bz2
# Source0-md5:	407d9f543ec533f85358c9166ff27a5c
Source1:	%{name}.desktop
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-datadir.patch
URL:		http://xut.dnteam.org
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel
#BuildRequires:	autoconf >= 2.61
#BuildRequires:	automake
BuildRequires:	cal3d-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XUT is a project to make a button football game simulation.

%description -l hu.UTF-8
XUT egy project, amelynek a célja egy gombfoci szimulátor létrehozása.

%description -l pl.UTF-8
XUT jest projektem "guzikowego" symulatora piłki nożnej.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
#%%{__aclocal}
#%%{__autoconf}
#%%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install data/xut-icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/xut.png

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xut
%{_datadir}/%{name}
%{_desktopdir}/xut.desktop
%{_pixmapsdir}/xut.png
