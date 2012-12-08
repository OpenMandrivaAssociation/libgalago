%define major 3
%define libname %mklibname galago %major
%define develname %mklibname galago -d

Summary: Base library of Galago 
Name: libgalago
Version: 0.5.2
Release: 1
Source0: http://www.galago-project.org/files/releases/source/libgalago/%{name}-%{version}.tar.bz2
License: LGPL
Group: System/Libraries
Url: http://www.galago-project.org/
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: gtk-doc


%description
This is the base library of the Galago desktop presence framework.

%package -n %libname
Group: System/Libraries
Summary: Base library of Galago - shared library
#gw for the translations
Requires: %name >= %version
#gw for the sharp bindings
Provides: galago%major = %version-%release

%description -n %libname
This is the base library of the Galago desktop presence framework.

%package -n %develname
Group: Development/C
Summary: Base library of Galago - headers
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release
Provides: galago-devel = %version-%release
Obsoletes: %mklibname galago 3 -d

%description -n %develname
This is the base library of the Galago desktop presence framework.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot} %name.lang
%makeinstall_std MKINSTALLDIRS=`pwd`/mkinstalldirs
rm -rf %buildroot%_datadir/autopackage
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS

%files -n %libname
%_libdir/lib*.so.%{major}*

%files -n %develname
%doc ChangeLog 
%_libdir/lib*.so
%_libdir/pkgconfig/libgalago.pc
%_includedir/%name/
%_datadir/gtk-doc/html/libgalago

