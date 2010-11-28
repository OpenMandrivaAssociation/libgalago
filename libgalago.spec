%define major 3
%define libname %mklibname galago %major
%define develname %mklibname galago -d

Summary: Base library of Galago 
Name: libgalago
Version: 0.5.2
Release: %mkrel 10
Source0: http://www.galago-project.org/files/releases/source/libgalago/%{name}-%{version}.tar.bz2
License: LGPL
Group: System/Libraries
Url: http://www.galago-project.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: dbus-glib-devel
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
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std MKINSTALLDIRS=`pwd`/mkinstalldirs
rm -rf %buildroot%_datadir/autopackage
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS NEWS

%files -n %libname
%defattr(-,root,root)
%_libdir/lib*.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc ChangeLog 
%_libdir/lib*.so
%attr(644,root,root) %_libdir/lib*.la
%_libdir/pkgconfig/libgalago.pc
%_includedir/%name/
%_datadir/gtk-doc/html/libgalago



