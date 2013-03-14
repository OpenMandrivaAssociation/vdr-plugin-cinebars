
%define plugin	cinebars
%define name	vdr-plugin-%plugin
%define version	0.0.5

Summary:	VDR plugin: Overlays "cinebars"
Name:		%name
Version:	%version
Release:	5
Group:		Video
License:	GPL+
URL:		http://www.egal-vdr.de/plugins/
Source:		http://www.egal-vdr.de/plugins/vdr-%plugin-%version.tgz
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Overlays "cinema-bars" over the live picture.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.5-4mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.5-3mdv2009.1
+ Revision: 359300
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.5-2mdv2009.0
+ Revision: 197912
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.5-1mdv2009.0
+ Revision: 197644
- new version
- add vdr_plugin_prep
- bump buildrequires on vdr-devel

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.4-3mdv2008.1
+ Revision: 145050
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4-2mdv2008.1
+ Revision: 103076
- rebuild for new vdr

* Fri Sep 07 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4-1mdv2008.0
+ Revision: 81865
- 0.0.4
- adapt license tag for new policy

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3a-10mdv2008.0
+ Revision: 49982
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3a-9mdv2008.0
+ Revision: 42069
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3a-8mdv2008.0
+ Revision: 22731
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3a-7mdv2007.0
+ Revision: 90904
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3a-6mdv2007.1
+ Revision: 73976
- rebuild for new vdr
- Import vdr-plugin-cinebars

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3a-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3a-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3a-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3a-2mdv2007.0
- rebuild for new vdr

* Wed Jun 21 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3a-1mdv2007.0
- initial Mandriva release

