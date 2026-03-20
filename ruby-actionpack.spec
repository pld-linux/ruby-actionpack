%define pkgname actionpack
Summary:	Object-Relational mapping library for Ruby
Summary(pl.UTF-8):	Biblioteka odwzorowań obiektowo-relacyjnych dla Ruby
Name:		ruby-%{pkgname}
Version:	8.1.2
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	b3ce9e5c668f7d810be3bf08a2167c57
URL:		https://rubyonrails.org
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
Requires:	ruby-actionview = %{version}
Requires:	ruby-activesupport = %{version}
Requires:	ruby-nokogiri >= 1.8.5
Requires:	ruby-rack >= 2.2.4
Requires:	ruby-rack-session >= 1.0.1
Requires:	ruby-rack-test >= 0.6.3
Requires:	ruby-rails-dom-testing >= 2.2
Requires:	ruby-rails-html-sanitizer >= 1.6.0
Requires:	ruby-useragent >= 0.16.0
Requires:	ruby >= 3.2.0
Provides:	ruby-ActionPack
Obsoletes:	ruby-ActionPack
BuildArch:	noarch
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

%package rdoc
Summary:	Documentation files for ActionPack
Summary(pl.UTF-8):	Dokumentacja do biblioteki ActionPack
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for ActionPack.

%description rdoc -l pl.UTF-8
Dokumentacja do biblioteki ActionPack.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

LC_ALL=en_US.UTF-8 rdoc --ri --op ri lib
LC_ALL=en_US.UTF-8 rdoc --op rdoc lib
rm ri/created.rid
rm ri/cache.ri
rm -fr ri/{system,Rack,CGI,FalseClass,HTML,Mime,NilClass,Object,RackLintPatch,Regexp,TrueClass}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{pkgname}-%{version}-%{release}

# install gemspec
install -d $RPM_BUILD_ROOT%{ruby_specdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md MIT-LICENSE README.rdoc
%{ruby_vendorlibdir}/abstract_controller
%{ruby_vendorlibdir}/abstract_controller.rb
%{ruby_vendorlibdir}/action_controller
%{ruby_vendorlibdir}/action_controller.rb
%{ruby_vendorlibdir}/action_dispatch
%{ruby_vendorlibdir}/action_dispatch.rb
%{ruby_vendorlibdir}/action_pack
%{ruby_vendorlibdir}/action_pack.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{pkgname}-%{version}-%{release}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/AbstractController
%{ruby_ridir}/ActionPack
%{ruby_ridir}/ActionController
%{ruby_ridir}/ActionDispatch
%{ruby_ridir}/lib/action_dispatch/journey/visualizer
