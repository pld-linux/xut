Summary:	A button football simulation
Summary(hu.UTF-8):	Gombfoci szimuláció
Name:		xut
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/digenv/%{name}_0_1_src.tar.bz2
# Source0-md5:	09baba4b462c5ac53a40aabfb7b2e7a9
URL:		http://xut.dnteam.org
BuildRequires:	OpenAL-devel
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	cal3d-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XUT is a project to make a button football game simulation.

%description -l hu.UTF-8
XUT egy project, amelynek a célja egy gombfoci szimulátor létrehozása.

%prep
%setup -q -n %{name}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/%{name}/%{name}-bin
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
