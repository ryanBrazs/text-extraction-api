package com.pi.pi_ods3.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.pi.pi_ods3.models.Medicamento;
import com.pi.pi_ods3.repository.MedicamentoRepository;

@Service
public class MedicamentoService {
    @Autowired
    private MedicamentoRepository repository;

    public List<Medicamento> listarTodos() {
        return repository.findAll();
    }

    public List<Medicamento> buscarPorNome(String nome) {
        return repository.findByNomeContainingIgnoreCase(nome);
    }
}
