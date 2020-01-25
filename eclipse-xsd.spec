%define		module		xsd
Summary:	XSD Schema Infoset Model
Summary(pl.UTF-8):	Model Infoset w schemacie XSD
Name:		eclipse-%{module}
Version:	2.2.5
Release:	1
License:	EPL v1.0
Group:		Libraries/Java
Source0:	http://archive.eclipse.org/modeling/emf/emf/downloads/drops/%{version}/R200808252119/xsd-SDK-%{version}.zip
# Source0-md5:	18eb2449902116d6eaa5b78f53c58b3b
URL:		http://eclipse.org/modeling/mdt/?project=xsd
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	eclipse >= 3.2
Requires:	eclipse-emf-sdo-xsd >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		eclipsedir	%{_datadir}/eclipse

%description
XSD Schema Infoset Model.

%description -l pl.UTF-8
Model Infoset w schemacie XSD.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{eclipsedir}/{features,plugins}
cp -a eclipse/features/* $RPM_BUILD_ROOT%{eclipsedir}/features
cp -a eclipse/plugins/* $RPM_BUILD_ROOT%{eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{eclipsedir}/features/org.eclipse.xsd*
%{eclipsedir}/plugins/org.eclipse.xsd*
%{eclipsedir}/plugins/org.eclipse.emf.mapping.xsd*
