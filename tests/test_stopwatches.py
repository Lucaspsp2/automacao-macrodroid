import pytest
import logging
from pages.stopwatches_page import StopwatchesPage

# Configuração do logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Handler para console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Handler para arquivo
file_handler = logging.FileHandler('test_stopwatches.log', mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# Formato do log
formatter = logging.Formatter(
    '%(asctime)s | %(levelname)-8s | %(funcName)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


class TestStopwatchesNavigation:
    """Testes relacionados à navegação para a página de Stopwatches."""

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        logger.info("=" * 60)
        logger.info("Iniciando setup do teste de navegação")
        self.page = StopwatchesPage(driver)
        self.page.open()
        self.page.wait_until_foreground()
        logger.info("Setup concluído. App está em foreground")

    def test_navigate_to_stopwatches_page(self):
        """Verifica se é possível navegar para a página de Stopwatches."""
        logger.info("Iniciando teste: Navegação para página de Stopwatches")
        
        logger.debug("Clicando no botão de Stopwatches")
        self.page.click_stopwatch_button()
        
        logger.debug("Verificando se a página de Stopwatches está visível")
        is_displayed = self.page.is_stopwatch_displayed()
        
        logger.info(f"Página de Stopwatches visível: {is_displayed}")
        assert is_displayed, "A página de Stopwatches não foi exibida corretamente"
        
        logger.info("Teste de navegação concluído com sucesso")


class TestStopwatchesCreation:
    """Testes relacionados à criação de Stopwatches."""

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        logger.info("=" * 60)
        logger.info("Iniciando setup do teste de criação")
        self.page = StopwatchesPage(driver)
        self.page.open()
        self.page.wait_until_foreground()
        
        # Navegar até a página de stopwatches
        logger.debug("Navegando para página de Stopwatches")
        self.page.click_stopwatch_button()
        assert self.page.is_stopwatch_displayed(), "Falha ao navegar para página de Stopwatches"
        logger.info("Setup concluído - Página de Stopwatches carregada")

    def test_create_new_stopwatch(self):
        """Verifica se é possível criar um novo Stopwatch."""
        logger.info("Iniciando teste: Criacao de novo Stopwatch")
        
        logger.debug("Clicando no botao de adicionar novo stopwatch")
        self.page.click_add_new_stopwatch()
        
        logger.debug("Preenchendo nome do stopwatch: 'automation_test'")
        self.page.name_stopwatch()
        
        logger.debug("Obtendo nome do stopwatch criado")
        stopwatch_name = self.page.get_stopwatch_name()
        logger.info(f"Nome do stopwatch obtido: '{stopwatch_name}'")
        
        assert "automation_test" in stopwatch_name, \
            f"Nome esperado 'automation_test' nao encontrado em '{stopwatch_name}'"
        
        # Cleanup: deletar o stopwatch criado
        logger.info("Iniciando cleanup: deletando stopwatch criado")
        logger.debug("Abrindo menu de contexto do stopwatch")
        self.page.click_clickable_stopwatch()
        logger.debug("Clicando na opcao de deletar")
        self.page.click_delete_stopwatch()
        logger.info("Cleanup concluido - Stopwatch deletado")
        
        logger.info("Teste de criacao concluido com sucesso")

    def test_add_stopwatch_button_is_clickable(self):
        """Verifica se o botão de adicionar stopwatch está clicável."""
        logger.info("Iniciando teste: Verificacao do botao de adicionar")
        
        logger.debug("Verificando se o botao FAB esta acessivel")
        self.page.click_add_new_stopwatch()
        self.page.name_stopwatch()
        
        # Cleanup: deletar o stopwatch criado
        logger.info("Iniciando cleanup: deletando stopwatch criado")
        self.page.click_clickable_stopwatch()
        self.page.click_delete_stopwatch()
        logger.info("Cleanup concluido - Stopwatch deletado")
        
        logger.info("Botao de adicionar stopwatch esta funcional")


class TestStopwatchesPlayPause:
    """Testes relacionados às funcionalidades de Play/Pause."""

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        logger.info("=" * 60)
        logger.info("Iniciando setup do teste de Play/Pause")
        self.page = StopwatchesPage(driver)
        self.page.open()
        self.page.wait_until_foreground()
        
        # Navegar e criar stopwatch
        logger.debug("Navegando para página de Stopwatches")
        self.page.click_stopwatch_button()
        assert self.page.is_stopwatch_displayed()
        
        logger.debug("Criando stopwatch para teste")
        self.page.click_add_new_stopwatch()
        self.page.name_stopwatch()
        logger.info("Setup concluído - Stopwatch criado para teste")

    def test_play_stopwatch(self):
        """Verifica se eh possivel iniciar o Stopwatch."""
        logger.info("Iniciando teste: Play do Stopwatch")
        
        logger.debug("Clicando no botao play/pause para iniciar")
        self.page.click_play_pause_button()
        
        # Cleanup: deletar o stopwatch criado
        logger.info("Iniciando cleanup: deletando stopwatch criado")
        self.page.click_clickable_stopwatch()
        self.page.click_delete_stopwatch()
        logger.info("Cleanup concluido - Stopwatch deletado")
        
        logger.info("Teste de play concluido com sucesso")

    def test_pause_stopwatch(self):
        """Verifica se eh possivel pausar o Stopwatch."""
        logger.info("Iniciando teste: Pause do Stopwatch")
        
        logger.debug("Clicando no botao play para iniciar")
        self.page.click_play_pause_button()
        
        logger.debug("Clicando no botao pause para pausar")
        self.page.click_play_pause_button()
        
        # Cleanup: deletar o stopwatch criado
        logger.info("Iniciando cleanup: deletando stopwatch criado")
        self.page.click_clickable_stopwatch()
        self.page.click_delete_stopwatch()
        logger.info("Cleanup concluido - Stopwatch deletado")
        
        logger.info("Teste de pause concluido com sucesso")

    def test_play_pause_toggle(self):
        """Verifica o toggle completo de Play/Pause."""
        logger.info("Iniciando teste: Toggle Play/Pause")
        
        logger.debug("Executando sequencia: Play -> Pause -> Play -> Pause")
        for i in range(4):
            action = "Play" if i % 2 == 0 else "Pause"
            logger.debug(f"Iteracao {i+1}: {action}")
            self.page.click_play_pause_button()
        
        # Cleanup: deletar o stopwatch criado
        logger.info("Iniciando cleanup: deletando stopwatch criado")
        self.page.click_clickable_stopwatch()
        self.page.click_delete_stopwatch()
        logger.info("Cleanup concluido - Stopwatch deletado")
        
        logger.info("Teste de toggle Play/Pause concluido com sucesso")


class TestStopwatchesClear:
    """Testes relacionados à funcionalidade de Clear."""

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        logger.info("=" * 60)
        logger.info("Iniciando setup do teste de Clear")
        self.page = StopwatchesPage(driver)
        self.page.open()
        self.page.wait_until_foreground()
        
        # Navegar e criar stopwatch
        self.page.click_stopwatch_button()
        self.page.click_add_new_stopwatch()
        self.page.name_stopwatch()
        logger.info("Setup concluído - Stopwatch criado para teste de Clear")

    def test_clear_stopwatch(self):
        """Verifica se eh possivel limpar o Stopwatch."""
        logger.info("Iniciando teste: Clear do Stopwatch")
        
        logger.debug("Iniciando stopwatch")
        self.page.click_play_pause_button()
        
        logger.debug("Pausando stopwatch")
        self.page.click_play_pause_button()
        
        logger.debug("Limpando stopwatch")
        self.page.click_clear_button()
        
        # Cleanup: deletar o stopwatch criado
        logger.info("Iniciando cleanup: deletando stopwatch criado")
        self.page.click_clickable_stopwatch()
        self.page.click_delete_stopwatch()
        logger.info("Cleanup concluido - Stopwatch deletado")
        
        logger.info("Teste de clear concluido com sucesso")

    def test_clear_after_play(self):
        """Verifica clear apos iniciar o stopwatch."""
        logger.info("Iniciando teste: Clear apos Play")
        
        logger.debug("Iniciando stopwatch")
        self.page.click_play_pause_button()
        
        logger.debug("Executando clear enquanto rodando")
        self.page.click_clear_button()
        
        # Cleanup: deletar o stopwatch criado
        logger.info("Iniciando cleanup: deletando stopwatch criado")
        self.page.click_clickable_stopwatch()
        self.page.click_delete_stopwatch()
        logger.info("Cleanup concluido - Stopwatch deletado")
        
        logger.info("Teste de clear apos play concluido com sucesso")


class TestStopwatchesRename:
    """Testes relacionados à funcionalidade de Rename."""

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        logger.info("=" * 60)
        logger.info("Iniciando setup do teste de Rename")
        self.page = StopwatchesPage(driver)
        self.page.open()
        self.page.wait_until_foreground()
        
        # Navegar e criar stopwatch
        self.page.click_stopwatch_button()
        self.page.click_add_new_stopwatch()
        self.page.name_stopwatch()
        logger.info("Setup concluído - Stopwatch criado para teste de Rename")

    def test_open_stopwatch_details(self):
        """Verifica se eh possivel abrir detalhes do Stopwatch."""
        logger.info("Iniciando teste: Abrir detalhes do Stopwatch")
        
        logger.debug("Clicando no stopwatch para abrir detalhes")
        self.page.click_clickable_stopwatch()
        
        # Cleanup: deletar o stopwatch criado
        logger.info("Iniciando cleanup: deletando stopwatch criado")
        self.page.click_delete_stopwatch()
        logger.info("Cleanup concluido - Stopwatch deletado")
        
        logger.info("Teste de abrir detalhes concluido com sucesso")

    def test_rename_stopwatch(self):
        """Verifica se eh possivel renomear o Stopwatch."""
        logger.info("Iniciando teste: Renomear Stopwatch")
        
        logger.debug("Abrindo menu de contexto do stopwatch")
        self.page.click_clickable_stopwatch()
        
        logger.debug("Clicando na opcao de renomear")
        self.page.click_rename_stopwatch()
        
        logger.debug("Verificando novo nome do stopwatch")
        new_name = self.page.get_stopwatch_name()
        logger.info(f"Novo nome obtido: '{new_name}'")
        
        assert "test_stopwatch" in new_name, \
            f"Nome esperado 'test_stopwatch' nao encontrado em '{new_name}'"
        
        # Cleanup: deletar o stopwatch criado
        logger.info("Iniciando cleanup: deletando stopwatch criado")
        self.page.click_clickable_stopwatch()
        self.page.click_delete_stopwatch()
        logger.info("Cleanup concluido - Stopwatch deletado")
        
        logger.info("Teste de rename concluido com sucesso")


class TestStopwatchesDelete:
    """Testes relacionados à funcionalidade de Delete."""

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        logger.info("=" * 60)
        logger.info("Iniciando setup do teste de Delete")
        self.page = StopwatchesPage(driver)
        self.page.open()
        self.page.wait_until_foreground()
        
        # Navegar e criar stopwatch
        self.page.click_stopwatch_button()
        self.page.click_add_new_stopwatch()
        self.page.name_stopwatch()
        logger.info("Setup concluído - Stopwatch criado para teste de Delete")

    def test_delete_stopwatch(self):
        """Verifica se é possível deletar o Stopwatch."""
        logger.info("Iniciando teste: Deletar Stopwatch")
        
        logger.debug("Abrindo menu de contexto do stopwatch")
        self.page.click_clickable_stopwatch()
        
        logger.debug("Clicando na opção de deletar")
        self.page.click_delete_stopwatch()
        
        logger.info("Teste de delete concluído com sucesso")


class TestStopwatchesFullFlow:
    """Teste de fluxo completo (E2E) do Stopwatches."""

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        logger.info("=" * 60)
        logger.info("Iniciando setup do teste E2E completo")
        self.page = StopwatchesPage(driver)
        self.page.open()
        self.page.wait_until_foreground()
        logger.info("Setup concluído")

    def test_full_stopwatch_flow(self):
        """Executa o fluxo completo: navegar, criar, play/pause, clear, rename, delete."""
        logger.info("Iniciando teste de fluxo completo E2E")
        
        # Navegar
        logger.info("STEP 1: Navegação")
        logger.debug("Clicando no botão de Stopwatches")
        self.page.click_stopwatch_button()
        assert self.page.is_stopwatch_displayed(), "Falha na navegação"
        logger.info("Navegação bem-sucedida")
        
        # Criar
        logger.info("STEP 2: Criação")
        logger.debug("Criando novo stopwatch")
        self.page.click_add_new_stopwatch()
        self.page.name_stopwatch()
        assert "automation_test" in self.page.get_stopwatch_name(), "Falha na criação"
        logger.info("Criação bem-sucedida")
        
        # Play/Pause
        logger.info("STEP 3: Play/Pause")
        logger.debug("Executando play")
        self.page.click_play_pause_button()
        logger.debug("Executando pause")
        self.page.click_play_pause_button()
        logger.info("Play/Pause bem-sucedido")
        
        # Clear
        logger.info("STEP 4: Clear")
        logger.debug("Limpando stopwatch")
        self.page.click_clear_button()
        logger.info("Clear bem-sucedido")
        
        # Rename
        logger.info("STEP 5: Rename")
        logger.debug("Abrindo detalhes")
        self.page.click_clickable_stopwatch()
        logger.debug("Renomeando stopwatch")
        self.page.click_rename_stopwatch()
        assert "test_stopwatch" in self.page.get_stopwatch_name(), "Falha no rename"
        logger.info("Rename bem-sucedido")
        
        # Delete
        logger.info("STEP 6: Delete")
        logger.debug("Abrindo detalhes para deletar")
        self.page.click_clickable_stopwatch()
        logger.debug("Deletando stopwatch")
        self.page.click_delete_stopwatch()
        logger.info("Delete bem-sucedido")
        
        logger.info("Teste de fluxo completo E2E finalizado com sucesso!")
