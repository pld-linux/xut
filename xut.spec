#
# TODO: - fix auto tools
#
%define		file_version %(echo %{version} | tr . _)
Summary:	A button football simulation
Summary(hu.UTF-8):	Gombfoci szimuláció
Summary(pl.UTF-8):	Symulator piłki nożnej
Name:		xut
Version:	0.2
Release:	0.1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/digenv/%{name}_%{file_version}_src.tar.bz2
# Source0-md5:	66c4bcd2ebc0fb5762bdea1df0db5a94
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-link.patch
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
BuildRequires:	sed >= 4.0
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

# remove ugly special chars from echo outputs
%{__sed} -i 's/\[0;32m//;s/\[0;0m//;s/\\e//g' `find -name Makefile.in`

%build
#%%{__aclocal}
#%%{__autoconf}
#%%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xut
%{_datadir}/%{name}
