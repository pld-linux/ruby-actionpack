Summary:	Object-Relational mapping library for Ruby
Summary(pl.UTF-8):	Biblioteka odwzorowań obiektowo-relacyjnych dla Ruby
Name:		ruby-ActionPack
Version:	2.0.5
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/45359/actionpack-%{version}.tgz
# Source0-md5:	3e63fec3ee33b9455306b8fb4e4a735f
URL:		http://rubyforge.org/projects/actionpack/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

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

%package rdoc
Summary:	Documentation files for ActionPack
Summary(pl.UTF-8):	Dokumentacja do biblioteki ActionPack
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for ActionPack.

%description rdoc -l pl.UTF-8
Dokumentacja do biblioteki ActionPack.

%prep
%setup -q -n actionpack-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -f ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}-%{release}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{ruby_rubylibdir}/action_controller
%{ruby_rubylibdir}/action_controller.rb
%{ruby_rubylibdir}/action_pack.rb
%{ruby_rubylibdir}/actionpack.rb
%{ruby_rubylibdir}/action_pack/version.rb
%{ruby_rubylibdir}/action_view
%{ruby_rubylibdir}/action_view.rb

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}-%{release}
%{ruby_ridir}/ri/ActionController
%{ruby_ridir}/ri/ActionPack
%{ruby_ridir}/ri/ActionView
%{ruby_ridir}/ri/CGI
%{ruby_ridir}/ri/ERB
%{ruby_ridir}/ri/FalseClass
%{ruby_ridir}/ri/HTML
%{ruby_ridir}/ri/Mime
%{ruby_ridir}/ri/NilClass
%{ruby_ridir}/ri/Object
%{ruby_ridir}/ri/Regexp
%{ruby_ridir}/ri/Test
%{ruby_ridir}/ri/TrueClass
