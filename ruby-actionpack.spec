%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
%define	ruby_version	%(ruby -r rbconfig -e 'print Config::CONFIG["ruby_version"]')
Summary:	Object-Relational mapping library for Ruby
Summary(pl):	Biblioteka odwzorowañ obiektowo-relacyjnych dla Ruby
Name:		ruby-ActionPack
%define tarname actionpack
Version:	1.5.1
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/3330/%{tarname}-%{version}.tgz
# Source0-md5:	56dca7c6188e3bd44074c2215f5aa9dd
URL:		http://actionpack.rubyonrails.org/
BuildRequires:	ruby
Requires:	ruby
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Action Pack splits the response to a web request into a controller
part (performing the logic) and a view part (rendering a template).
This two-step approach is known as an action, which will normally
create, read, update, or delete (CRUD for short) some sort of model
part (often database) before choosing either to render a template or
redirecting to another action.

%description -l pl
Action Pack dzieli odpowied¼ na ¿±danie WWW na czê¶æ steruj±c±
(wykonuj±c± logikê) i czê¶æ widokow± (przetwarzaj±c± szablon). To
dwukrokowe podej¶cie jest znane jako akcja, która zwykle tworzy,
czyta, uaktualnia lub usuwa (create, read, update, delete - CRUD)
jaki¶ rodzaj czê¶ci modelu (zwykle bazy danych) przed wybraniem czy
przetwarzaæ szablon, czy przekierowaæ do innej akcji.

%prep
%setup -q -n %{tarname}-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README rdoc
%{ruby_rubylibdir}/*
%{ruby_ridir}/ActionController
%{ruby_ridir}/ActionView
%{ruby_ridir}/CGIMethods
