

# features for testing

Feature: Testing API responses

  Scenario: Compare birthday deeplink
    Given Test "birthday_deeplink" get-request
    
  Scenario: Compare buy more  
    Given Test "buy_more" get-request

  Scenario: Compare cheers
    Given Test "cheers" get-request

  Scenario: Compare configs
    Given Test "configs" get-request

  Scenario: Compare country
    Given Test "country" get-request

  Scenario: Compare deep links
    Given Test "deep_links_not_working" get-request
    And Test "deep_links_not_working_as_expected_brunch" get-request

  Scenario: Compare delivery status
    Given Test "delivery_status" get-request
    And Test "delivery_status_with_multiple_filters" get-request

  Scenario: Compare dempgraphic state
    Given Test "demographic_state" post-request

  Scenario: Compare friends rankings
    Given Test "friends_rankings" get-request

  Scenario: Compare home
    Given Test "home" get-request

  Scenario: Compare hotels
    Given Test "hotels" get-request

  Scenario: Compare invalid id
    Given Test "invalid_id" get-request

  Scenario: Compare merchants
    Given Test "merchants" get-request
    And Test "merchant_outlets_with_id" get-request
    And Test "merchant_with_id" get-request
    And Test "merchant_empty_search_scope" get-request
    And Test "merchant_search_scope" get-request
    And Test "merchant_names" get-request
    And Test "merchant_name" get-request
    And Test "es_merchant_with_id" get-request elastic search

  Scenario: Compare naming issue
    Given Test "naming_issue" get-request

  Scenario: Compare offers
    Given Test "offers" get-request

  Scenario: Compare outlets
    Given Test "outlets" get-request with missing arguments
    And Test "outlet_names_without_offer_id" get-request

  Scenario: Compare outlets without id
    Given Test "outlet_names_with_offer_id" get-request with different urls for php and python

  Scenario: Compare outlets with elastic search
    Given Test "es_outlets" get-request elastic search

  Scenario: Compare redemption
    Given Test "redemption" post-request different data
    And Test "redemption_sync" post-request different data

  Scenario: Compare offers
    Given Test "send_offer" post-request
    And Test "accept_offer" post-request

  Scenario: Compare sessions
    Given Test "sessions" post-request

  Scenario: Compare sharing
    Given Test "sharing_send_offers" get-request
    And Test "sharing_receive_offers" get-request

  Scenario: Compare savings
    Given Test "showing_savings" get-request

  Scenario: Compare smiles
    Given Test "smiles" get-request
    And Test "smiles_purchase" post-request

  Scenario: Compare user
    Given Test "user_products" get-request
    And Test "user_profile" get-request
    And Test "user" get-request



