Name:           maven-changes-plugin
Version:        2.4
Release:        3
Summary:        Plugin to support reporting of changes between releases

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/%{name}
# svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-changes-plugin-2.4
# tar caf maven-changes-plugin-2.4.tar.xz maven-changes-plugin-2.4
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.depmap

# patches not upstreamed yet, tests need to  be fixed to work with new
# doxia too
Patch0:         0001-xmlrpc3-common-dependency.patch
Patch1:         0002-doxia-1.1-import-fix.patch


BuildArch:      noarch

BuildRequires: java-devel >= 0:1.6.0
BuildRequires: plexus-utils
BuildRequires: ant-nodeps
BuildRequires: maven
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-shared-filtering
BuildRequires: plexus-maven-plugin
BuildRequires: plexus-mail-sender
BuildRequires: xmlrpc3-client
BuildRequires: xmlrpc3-common
BuildRequires: xerces-j2
BuildRequires: xml-commons-apis

Requires: maven2
Requires: jpackage-utils
Requires: java
Requires(post): jpackage-utils
Requires(postun): jpackage-utils

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
Group:    Development/Java
Summary:  Javadoc for %{name}
Requires: jpackage-utils

%description javadoc
API documentation for %{name}.


%prep
%setup -q #You may need to update this according to your Source0
%patch0 -p1
%patch1 -p1

%build
mvn-rpmbuild -e -X \
        -Dmaven.local.depmap.file="%{SOURCE1}" \
        -Dmaven.test.skip=true \
        install javadoc:javadoc

%install

# jars
install -Dpm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%add_to_maven_depmap org.apache.maven.plugins %{name} %{version} JPP %{name}

# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%pre javadoc
# workaround for rpm bug, can be removed in F-18
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :


%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%defattr(-,root,root,-)
%{_javadir}/*
%{_mavenpomdir}/*
%config(noreplace) %{_mavendepmapfragdir}/*

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}

