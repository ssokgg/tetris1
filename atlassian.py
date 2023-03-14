- text: >
    oauthEndpoint = oauth2.Endpoint{
    +       AuthURL:  "https://auth.atlassian.com/authorize",
    +       TokenURL: "https://auth.atlassian.com/oauth/token",
    +   }
    +   oauthConfig = &oauth2.Config{
    +       RedirectURL:  "http://localhost:3000/auth/jira/callback",
    +       ClientID:     "W4XTi79CmCvhnWYszR70dypEQFtHA3qH",
    +       ClientSecret: "CXEQC92LBtFAchTsuHnFcf_0if7t8KhFxgM_68dNHKYxZ--n6PwSRFyEckem6X9n",
    +       Scopes:       []string{"read:jira-user", "read:jira-work", "offline_access"},
    +       Endpoint:     oauthEndpoint,
    +   }
    +)

  client_id: W4XTi79CmCvhnWYszR70dypEQFtHA3qH
  client_secret: CXEQC92LBtFAchTsuHnFcf_0if7t8KhFxgM_68dNHKYxZ--n6PwSRFyEckem6X9n

