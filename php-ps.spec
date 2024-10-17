%define modname ps
%define dirname %{modname}
%define soname %{modname}.so
%define inifile A53_%{modname}.ini

Summary:	An extension to create PostScript files for php
Name:		php-%{modname}
Version:	1.3.7
Release:	2
Group:		Development/PHP
License:	PHP License
URL:		https://pecl.php.net/package/ps
Source0:	http://pecl.php.net/get/ps-%{version}.tgz
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	pslib-devel >= 0.4.1
BuildRequires:	libgd-devel
Requires:	php-imagick

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

%files 
%defattr(-,root,root)
%doc CREDITS tests examples package.xml
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}


%changelog
* Sun May 06 2012 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-25mdv2012.0
+ Revision: 797044
- fix build
- rebuild for php-5.4.x
- rebuild

* Thu Nov 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-23
+ Revision: 715673
- fix deps
- fix #60170 (a dependancy is missing. php-ps)

* Wed Aug 24 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-22
+ Revision: 696457
- rebuilt for php-5.3.8

* Fri Aug 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-21
+ Revision: 695452
- rebuilt for php-5.3.7

* Sat Mar 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-20
+ Revision: 646673
- rebuilt for php-5.3.6

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-19mdv2011.0
+ Revision: 629853
- rebuilt for php-5.3.5

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-18mdv2011.0
+ Revision: 628173
- ensure it's built without automake1.7

* Wed Nov 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-17mdv2011.0
+ Revision: 600520
- rebuild

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-16mdv2011.0
+ Revision: 588857
- rebuild

* Fri Mar 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-15mdv2010.1
+ Revision: 514640
- rebuilt for php-5.3.2

* Sat Jan 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-14mdv2010.1
+ Revision: 485420
- rebuilt for php-5.3.2RC1

* Sat Nov 21 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-13mdv2010.1
+ Revision: 468238
- rebuilt against php-5.3.1

* Wed Sep 30 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-12mdv2010.0
+ Revision: 451347
- rebuild

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 1.3.6-11mdv2010.0
+ Revision: 397582
- Rebuild

* Mon May 18 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-10mdv2010.0
+ Revision: 377018
- rebuilt for php-5.3.0RC2

* Sun Mar 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-9mdv2009.1
+ Revision: 346597
- rebuilt for php-5.2.9

* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-8mdv2009.1
+ Revision: 341788
- rebuilt against php-5.2.9RC2

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-7mdv2009.1
+ Revision: 323036
- rebuild

* Fri Dec 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-6mdv2009.1
+ Revision: 310297
- rebuilt against php-5.2.7

* Fri Jul 18 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-5mdv2009.0
+ Revision: 238421
- rebuild

* Fri May 02 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-4mdv2009.0
+ Revision: 200260
- rebuilt for php-5.2.6

* Sun Feb 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-3mdv2008.1
+ Revision: 169562
- fix deps

* Mon Feb 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-2mdv2008.1
+ Revision: 162235
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 27 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-1mdv2008.1
+ Revision: 113374
- 1.3.6

* Sun Nov 11 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.5-3mdv2008.1
+ Revision: 107710
- restart apache if needed

* Sat Sep 01 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.5-2mdv2008.0
+ Revision: 77568
- rebuilt against php-5.2.4

* Fri Jul 13 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.5-1mdv2008.0
+ Revision: 51779
- fix deps
- use the new %%serverbuild macro
- 1.3.5

* Thu Jun 14 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-7mdv2008.0
+ Revision: 39516
- use distro conditional -fstack-protector

* Fri Jun 01 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-6mdv2008.0
+ Revision: 33869
- rebuilt against new upstream version (5.2.3)

* Thu May 03 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-5mdv2008.0
+ Revision: 21349
- rebuilt against new upstream version (5.2.2)


* Thu Feb 08 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-4mdv2007.0
+ Revision: 117607
- rebuilt against new upstream version (5.2.1)

* Wed Nov 08 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-3mdv2007.0
+ Revision: 78097
- rebuilt for php-5.2.0
- Import php-ps

* Mon Aug 28 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-2
- rebuilt for php-5.1.6

* Fri Aug 04 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-1mdv2007.0
- initial Mandriva package


