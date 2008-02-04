%define modname ps
%define dirname %{modname}
%define soname %{modname}.so
%define inifile A53_%{modname}.ini

Summary:	An extension to create PostScript files for php
Name:		php-%{modname}
Version:	1.3.6
Release:	%mkrel 2
Group:		Development/PHP
License:	PHP License
URL:		http://pecl.php.net/package/%{modname}
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	libpslib-devel
BuildRequires:	libgd-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
ps is an extension similar to the pdf extension but for creating PostScript
files. Its api is modelled after the pdf extension.

%prep

%setup -q -n %{modname}-%{version}
[ "../package.xml" != "/" ] && mv ../package.xml .

%build
%serverbuild

phpize
%configure2_5x --with-libdir=%{_lib} \
    --with-%{modname}=shared,%{_prefix}
%make

mv modules/*.so .

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m0755 %{soname} %{buildroot}%{_libdir}/php/extensions/

cat > %{buildroot}%{_sysconfdir}/php.d/%{inifile} << EOF
extension = %{soname}
EOF

%post
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CREDITS tests examples package.xml
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}
