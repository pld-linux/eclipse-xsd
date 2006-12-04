%define		module xsd
Summary:	XSD Schema Infoset Model
Name:		eclipse-%{module}
Version:	2.2.1
Release:	0.1
License:	CPL
Group:		Development/Tools
Source0:	http://download.eclipse.org/tools/emf/downloads/drops/%{version}/R200609210005/%{module}-SDK-%{version}.zip
# Source0-md5:	52dc08d87d41e65b7c442bea868ee71c
#URL:		
BuildRequires:	unzip
Requires:	eclipse >= 3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_eclipsedir	%{_datadir}/eclipse

%description
XSD Schema Infoset Model.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}
cp -rf eclipse/features/* $RPM_BUILD_ROOT%{_eclipsedir}/features
cp -rf eclipse/plugins/* $RPM_BUILD_ROOT%{_eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_eclipsedir}/features/org.eclipse.xsd*
%{_eclipsedir}/plugins/org.eclipse.xsd*
