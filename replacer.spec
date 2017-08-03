%{?scl:%scl_package replacer}
%{!?scl:%global pkg_name %{name}}

Name:          %{?scl_prefix}replacer
Version:       1.6
Release:       4.2%{?dist}
Summary:       Replacer Maven Mojo
License:       MIT
URL:           https://github.com/beiliubei/maven-replacer-plugin
# http://code.google.com/p/maven-replacer-plugin/
Source0:       https://github.com/beiliubei/maven-replacer-plugin/archive/%{version}.tar.gz

BuildRequires: %{?scl_prefix}maven-local
BuildRequires: %{?scl_prefix}mvn(commons-io:commons-io)
BuildRequires: %{?scl_prefix}mvn(commons-lang:commons-lang)
BuildRequires: %{?scl_prefix}mvn(junit:junit)
BuildRequires: %{?scl_prefix}mvn(org.apache.ant:ant)
BuildRequires: %{?scl_prefix}mvn(org.apache.maven:maven-plugin-api)
BuildRequires: %{?scl_prefix}mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: %{?scl_prefix}mvn(org.hamcrest:hamcrest-all)
BuildRequires: %{?scl_prefix}mvn(org.mockito:mockito-all)
BuildRequires: %{?scl_prefix}mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: %{?scl_prefix}mvn(xerces:xercesImpl)
BuildRequires: %{?scl_prefix}mvn(xml-apis:xml-apis)

BuildArch:     noarch

%description
Maven plugin to replace tokens in a given file with a value.

This plugin is also used to automatically generating PackageVersion.java
in the FasterXML.com project.

%package javadoc
Summary:       Javadoc for %{pkg_name}

%description javadoc
This package contains javadoc for %{pkg_name}.

%prep
%setup -q -n maven-replacer-plugin-%{version}

%pom_remove_plugin :dashboard-maven-plugin
%pom_remove_plugin :maven-assembly-plugin
# NoClassDefFoundError: org/w3c/dom/ElementTraversal
%pom_add_dep xml-apis:xml-apis::test

sed -i.hamcrest '/startsWith/d' src/test/java/com/google/code/maven_replacer_plugin/file/FileUtilsTest.java

%mvn_file :%{pkg_name} %{pkg_name}
%mvn_alias :%{pkg_name} com.google.code.maven-replacer-plugin:maven-replacer-plugin

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 1.6-4.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1.6-4.1
- Automated package import and SCL-ization

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 17 2015 gil cattaneo <puntogil@libero.it> 1.6-1
- update to 1.6
- fix Url tag and Source0 tag

* Wed Feb 11 2015 gil cattaneo <puntogil@libero.it> 1.5.3-2
- introduce license macro

* Thu Jul 03 2014 gil cattaneo <puntogil@libero.it> 1.5.3-1
- update to 1.5.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.5.2-4
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 gil cattaneo <puntogil@libero.it> 1.5.2-2
- switch to XMvn
- minor changes to adapt to current guideline

* Sun May 26 2013 gil cattaneo <puntogil@libero.it> 1.5.2-1
- initial rpm
