Summary:	Object-Relational mapping library for Ruby
Summary(pl.UTF-8):   Biblioteka odwzorowań obiektowo-relacyjnych dla Ruby
Name:		ruby-ActionPack
%define tarname actionpack
Version:	1.12.5
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/download.php/12314/%{tarname}-%{version}.tgz
# Source0-md5:	75d97cc7c91f036400a94ed8f2d49b2c
URL:		http://actionpack.rubyonrails.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Action Pack splits the response to a web request into a controller
part (performing the logic) and a view part (rendering a template).
This two-step approach is known as an action, which will normally
create, read, update, or delete (CRUD for short) some sort of model
part (often database) before choosing either to render a template or
redirecting to another action.

%description -l pl.UTF-8
Action Pack dzieli odpowiedź na żądanie WWW na część sterującą
(wykonującą logikę) i część widokową (przetwarzającą szablon). To
dwukrokowe podejście jest znane jako akcja, która zwykle tworzy,
czyta, uaktualnia lub usuwa (create, read, update, delete - CRUD)
jakiś rodzaj części modelu (zwykle bazy danych) przed wybraniem czy
przetwarzać szablon, czy przekierować do innej akcji.

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
