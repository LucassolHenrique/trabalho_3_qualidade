Feature: Login no Local Eats
  Como um usuário registrado
  Eu quero entrar na minha conta
  Para que eu possa fazer pedidos de comida

  Scenario: Login com sucesso
    Given que eu estou na página de login do Local Eats
    When eu insiro o e-mail "Lucas.oliveira@teste.com" e a senha "123456"
    And eu clico no botão de entrar
    Then eu devo ser redirecionado para a página inicial
