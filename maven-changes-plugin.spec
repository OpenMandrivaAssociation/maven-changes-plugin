%{?_javapackages_macros:%_javapackages_macros}
Name:           maven-changes-plugin
Version:        2.8
Release:        9.1
Summary:        Plugin to support reporting of changes between releases


License:        ASL 2.0
URL:            http://maven.apache.org/plugins/%{name}
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:         0001-Remove-dependency-on-velocity-tools.patch
Patch1:		0002-Update-to-Doxia-1.6.patch

BuildArch:      noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: apache-commons-collections
BuildRequires: jakarta-commons-httpclient
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-logging
BuildRequires: maven-local
BuildRequires: maven-project
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-shared-filtering
BuildRequires: maven-shared-reporting-api
BuildRequires: maven-shared-reporting-impl
BuildRequires: modello
BuildRequires: plexus-containers-container-default
BuildRequires: plexus-containers-component-metadata
BuildRequires: plexus-mail-sender
BuildRequires: plexus-i18n
BuildRequires: plexus-interpolation
BuildRequires: plexus-utils
BuildRequires: plexus-velocity
BuildRequires: xmlrpc3-client
BuildRequires: xmlrpc3-common
BuildRequires: xerces-j2
BuildRequires: xml-commons-apis
BuildRequires: velocity

Obsoletes: maven2-plugin-changes <= 0:2.0.8
Provides: maven2-plugin-changes = 1:%{version}-%{release}

%description
This plugin is used to inform your users of the changes that have
occurred between different releases of your project. The plugin can
extract these changes, either from a changes.xml file or from the JIRA
issue management system, and present them as a report. You also have
the option of creating a release announcement and even sending this
via email to your users.


%package javadoc

Summary:  Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -q

# remove dependency on velocity-tools
%patch0 -p1
%patch1 -p1
%pom_remove_dep :velocity-tools

# Javamail is provided by JDK
%pom_remove_dep :geronimo-javamail_1.4_mail
%pom_remove_dep :geronimo-javamail_1.4_provider
%pom_remove_dep :geronimo-javamail_1.4_spec

# Fix Maven 3 compatibility
%pom_add_dep org.apache.maven:maven-compat

# Disable github module as we don't have dependencies
rm -rf src/main/java/org/apache/maven/plugin/github
%pom_remove_dep org.apache.httpcomponents:
%pom_remove_dep org.eclipse.mylyn.github:

%build
%mvn_build -f

%install
%mvn_install


%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 10 2013 Michal Srb <msrb@redhat.com> - 2.8-5
- Remove dependency on velocity-tools

* Tue Feb 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.8-4
- Use default packaging layout

* Tue Feb 12 2013 Michal Srb <msrb@redhat.com> - 2.8-3
- Build with xmvn
- Remove custom depmap

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.8-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Sep 17 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.8-1
- Update to upstream version 2.8
- Convert patches to POM macros
- Install LICENSE and NOTICE files
- Remove rpm bug workaround

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 24 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.7.1-1
- Update to latest upstream (2.7.1)
- Remove upstreamed patch for component-metadata migration

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 15 2011 Jaromir Capik <jcapik@redhat.com> 2.6-2
- Migration from plexus-maven-plugin to plexus-containers-component-metadata

* Mon Jun 27 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.6-1
- Update to latest upstream (2.6)
- Properly complete BR/R
- Fix maven3 compatibility

* Tue May 24 2011 Alexander Kurtakov <akurtako@redhat.com> 2.5-2
- Do not require maven2, require maven.

* Tue May 24 2011 Alexander Kurtakov <akurtako@redhat.com> 2.5-1
- Update to latest upstream - 2.5.

* Fri Mar  4 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4-1
- Update to latest upsteam (2.4)
- Build with maven 3
- Versionless jars & javadocs

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.3-1
- Initial package
