%define 	modulename	pam_radius
Summary:	PAM module to authenticate using RADIUS server
Summary(pl.UTF-8):	Moduł PAM pozwalający na użycie serwera RADIUS do uwierzytelniania
Name:		pam-%{modulename}_auth
Version:	1.4.0
Release:	1
License:	GPL
Group:		Networking
Source0:	ftp://ftp.freeradius.org/pub/radius/%{modulename}-%{version}.tar.gz
# Source0-md5:	80960fdc9b720677dbb51d17311664a0
URL:		http://www.freeradius.org/pam_radius_auth/
BuildRequires:	pam-devel > 0.77.3-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the PAM to RADIUS authentication module. It allows any
PAM-capable machine to become a RADIUS client for authentication and
accounting requests. You will need a RADIUS server to perform the
actual authentication.

%description -l pl.UTF-8
To jest moduł PAM służący do uwierzytelniania użytkowników względem
serwera RADIUS. Pozwala każdej maszynie korzystającej z PAM zostać
klientem usługi RADIUS w celach uwierzytelniania użytkowników oraz
zbierania statystyk logowań (accounting). Do dokonania samego
uwierzytelnienia niezbędny jest serwer RADIUS.

%prep
%setup -q -n %{modulename}-%{version}

%build
%configure \
	ac_cv_lib_nsl_inet_ntoa=no \
	ac_cv_lib_resolv_inet_aton=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/%{_lib}/security,%{_sysconfdir}/raddb}

install pam_radius_auth.so $RPM_BUILD_ROOT/%{_lib}/security
cp -p pam_radius_auth.conf $RPM_BUILD_ROOT%{_sysconfdir}/raddb/server

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog LICENSE README.rst TODO USAGE
# dir shared with server package
%dir %{_sysconfdir}/raddb
%attr(640,root,root) %config(noreplace) %{_sysconfdir}/raddb/server
%attr(755,root,root) /%{_lib}/security/pam_radius_auth.so
