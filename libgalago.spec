%define major	3
%define libname	%mklibname galago %{major}
%define devname	%mklibname galago -d

Summary:	Base library of Galago 
Name:		libgalago
Version:	0.5.2
Release:	5
License:	LGPLv2
Group:		System/Libraries
Url:		http://www.galago-project.org/
Source0:	http://www.galago-project.org/files/releases/source/libgalago/%{name}-%{version}.tar.bz2
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(dbus-glib-1)

%description
This is the base library of the Galago desktop presence framework.

%package -n %{libname}
Summary:	Base library of Galago - shared library
Group:		System/Libraries
#gw for the translations
Requires:	%{name} >= %{version}
#gw for the sharp bindings
Provides:	galago%{major} = %{version}-%{release}

%description -n %{libname}
This is the base library of the Galago desktop presence framework.

%package -n %{devname}
Summary:	Base library of Galago - headers
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This is the base library of the Galago desktop presence framework.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std MKINSTALLDIRS=`pwd`/mkinstalldirs
rm -rf %buildroot%{_datadir}/autopackage
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS NEWS

%files -n %{libname}
%{_libdir}/libgalago.so.%{major}*

%files -n %{devname}
%doc ChangeLog 
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/libgalago.pc
%{_includedir}/%{name}/
%{_datadir}/gtk-doc/html/libgalago

